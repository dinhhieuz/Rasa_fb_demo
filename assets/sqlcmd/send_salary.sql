-- table
Select * from dbo.dsa_hieu_salary
select * from list_salary_OTN order by stt DESC
select stt from list_salary_OTN Where token_otn = '2250273222603605466'
select * from list_salary_OTN where send_id = '4857932260991004'  and year(date_mfg) = year(getdate()) and MONTH(date_mfg) = month(getdate()) and date_exec is null
GO
------------------
insert into dsa_hieu_salary
                values ('1','4857932260991004',5,N'Trần Đình Hiếu','01.01.00.00',N'Chủ tịch',30005593,802559461,69821437,2022,3)
------------------
--exec dsa_proc_salary_send N'4857932260991004', N'2250273222603605466'
insert into dsa_hieu_salary
            values ('1','4857932260991004',5,N'Trần Đình Hiếu','01.01.00.00',N'Chủ tịch',170786459,189162205,224511543,2022,4)
--NOTE: PROCEDURE OF CREATE SEND SALARY WITH TOKEN 
--USE [test_chatbot]
GO
/****** Object:  StoredProcedure [dbo].[dsa_proc_salary_send]    Script Date: 3/23/2022 4:48:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

--exec dsa_proc_salary_send N'4857932260991004', N'8227548954713778110'

ALTER Procedure [dbo].[dsa_proc_salary_send] (
    @send_id nvarchar(20),
    @token_otn nvarchar(30)
)
as
begin
	If (Select count(stt) from list_salary_OTN where token_otn = @token_otn) < 1
	begin
		declare 
			  @stt int = (select max(stt)+1 from dbo.list_salary_OTN)
			, @date_mfg date = getdate() --Manufacturing Date
			, @date_exp date = dateadd(year, 1, getdate()) -- Expire
			, @date_exec date = Null -- Date execute token
		insert into list_salary_OTN
		VALUES
			(@stt, @send_id, @token_otn, @date_mfg, @date_exp, @date_exec)

		--if @@ROWCOUNT = 1
		--	select 'true' as check_reg
		--else
		--	select 'false' as check_reg
	end
--    exec dsa_proc_salary_send N'4857932260991004', N'1758672770009085094'
End

go

insert into dsa_hieu_salary
values
('1','4857932260991004',5,N'Trần Đình Hiếu','01.01.00.00',N'Chủ tịch',916765874,402262451,514503423,2021,10)

----------------NOTE: TRIGGER 
alter TRIGGER dsa_trg_salary_send
ON dbo.dsa_hieu_salary 
FOR INSERT, UPDATE,DELETE
AS
BEGIN
	print('hi')
	select * from dbo.dsa_hieu_salary 
    -- Bảng ảo chứa lương tháng này
    select * into #salary 
    from dbo.dsa_hieu_salary 
    where   
        year_l = year(getdate()) 
        and month_l = month(getdate()) - 1

    -- Xét điều kiện xem có lương tháng này chưa
    --if ( select count(ma_nv) from #salary ) = 10
    --    and 
    --   ( select count(ma_nv) from #salary where con_lai is null ) = 0 
	IF 1=1
    begin
        -- True: Thực hiện gữi tin cho khách hàng bằng code python
		
		
        Declare @input_data Nvarchar(max) = N'
            select Top 1 * from (select distinct
					s.stt as "stt_l", ma_nv, id_fb, ten_nv, ten_bp, thu_nhap, tinh_tru, con_lai, year_l, month_l, 
					o.stt as "stt_o", send_id, token_otn, date_mfg, date_exp, date_exec
				from dbo.dsa_hieu_salary s RIGHT JOIN dbo.list_salary_OTN o on s.id_fb =  o.send_id
				where 
					o.date_exec is null 
					and o.date_exp >= getdate() 
				) as A
			order by year_l DESC, month_l Desc  '
            -- select * from dbo.dsa_hieu_salary s RIGHT JOIN dbo.list_salary_OTN o on s.id_fb =  o.send_id
		--Tạo bảng ảo lưu kết quả
		DECLARE @RESULT_POST TABLE (
			check_send varchar(10),
			token_otn varchar(30)
			
		)
		-- Gữi bảng lương cho khách hàng
        INSERT INTO @RESULT_POST EXECUTE sp_execute_external_script @language = N'Python'
            , @script = N'
db = InputDataSet
import requests
import json
import pandas as pd

#df_check = pd.DataFrame(columns=["token_otn","check_send"])
df_check = []
access_token = "EAAdiPQ5GoRsBAP8CbV8ayUyIar6Suy8yYug57vUVTnJURUDhrs1Rspon6oRL799gbF3ZA9dMoOwy43CmSFCD92kyLp7bVGxYF6jjZCV5PdrZAXB77aBenruRxGea0ZBz5hsZBJIitIyfnDFgVRinD4cCgMnA75vcKmgtaA7vZBZBzIMY53h5biB"
end_point = f"https://graph.facebook.com/v13.0/me/messages?access_token={access_token}"

for i in range(len(db)):
    contents = """
Bảng tiền lương của tháng {0} năm {1}:\n   Tên: {2} (mã nv: {3})\n   Bộ phận: {4}\n      + Thu nhập: {5}\n      + Ứng trước: {6}\n      + Còn lại: {7}\n
""".format(db["month_l"][i], db["year_l"][i], db["ten_nv"][i], db["ma_nv"][i], db["ten_bp"][i], db["thu_nhap"][i], db["tinh_tru"][i], db["con_lai"][i])
    notice_token = db["token_otn"][i]
    payload = {
                "recipient": {
                    "one_time_notif_token": notice_token
                },
                "message": {
                    "text": contents
                }
              }
    response = requests.post(end_point, data=json.dumps(payload), headers={"content-type": "application/json"}).json()
    if "error" in response.keys():
        check = "false"
    else:
        check = "true"

    df_check.append({"check_send":check, "token_otn": notice_token})
OutputDataSet = pd.DataFrame.from_dict(df_check, orient="columns")
print(OutputDataSet)
                '
            , @input_data_1 = @input_data; 

			-- Check sending API results to Employees 
			select * from @RESULT_POST

			update list_salary_OTN
			SET date_exec = iif(r.check_send = 'true', convert(date,getdate()), convert(date,'0001-01-01'))
			FROM @RESULT_POST r left join list_salary_OTN l 
				 ON r.token_otn = l.token_otn
			WHERE 
				l.token_otn = r.token_otn

    end
end
--------------------------------------------------------------



EXECUTE sp_execute_external_script @language = N'Python'
    , @script = N'
import requests
response = requests.get(url = "https://6237d6d9f5f6e28a154f3fa2.mockapi.io/add")
print(response)
        '
EXECUTE sp_execute_external_script @language = N'Python'
    , @script = N'
import pandas as pd
df_check = []
for i in range(4):
    df_check.append({"token_otn": 1, "check_send":1})
print(pd.DataFrame.from_dict(df_check, orient="columns"))
        '


--!--------------------------END

--!--------------------------------------------
--------------# Create table Salary_OTN

-- create table list_salary_OTN (
--     stt int,
--     send_id nvarchar(20),
--     token_otn nvarchar(30),
--     date_mfg date, --Manufacturing Date
--     date_exp date, -- Expire
--     date_exec date -- Date execute token
-- )

-- insert into list_salary_OTN
-- VALUES
--     (1, '4857932260991004', '7089066037755021622', '2022-03-01','2023-03-01',Null)
--     ,(2, '4857932260991004', '7089066037755021321', '2022-03-02','2023-03-02',Null)
    
------------# Create table salary

-- CREATE TABLE dsa_hieu_salary (
--     ma_nv nvarchar(5),
--     id_fb nvarchar(20),
--     stt int,
--     ten_nv nvarchar(100),
--     ma_bp nvarchar(15),
--     ten_bp nvarchar(100),
--     thu_nhap int,
--     tinh_tru int,
--     con_lai int,
--     year_l int,
--     month_l int
-- ) 
insert into dsa_hieu_salary values ('1','4857932260991004',5,N'Trần Đình Hiếu','01.01.00.00',N'Chủ tịch',916765874,402262451,514503423,2021,10)
,
-- ('99','4018044136324180',5,N'Nguyễn Ngọc Sơn','01.01.00.00',N'Ban Giám đốc',916765874,402262451,514503423,2021,11),
-- ('99','4371512817548370',5,N'Nguyễn Ngọc Sơn','01.01.00.00',N'Ban Giám đốc',916765874,402262451,514503423,2021,12),
-- ('99','4589490576059930',5,N'Nguyễn Ngọc Sơn','01.01.00.00',N'Ban Giám đốc',916765874,402262451,514503423,2021,9),
-- ('99','4718301048584870',5,N'Nguyễn Ngọc Sơn','01.01.00.00',N'Ban Giám đốc',916765874,402262451,514503423,2022,1),
-- ('99','4902896611320960',5,N'Nguyễn Ngọc Sơn','01.01.00.00',N'Ban Giám đốc',916765874,402262451,514503423,2022,2),
-- ('136','4659237040989400',6,N'Nguyễn Quang Trung','01.01.00.00',N'Ban Giám đốc',756563473,338675425,417888048,2021,10),
-- ('136','4953176568666510',6,N'Nguyễn Quang Trung','01.01.00.00',N'Ban Giám đốc',756563473,338675425,417888048,2021,11),
-- ('136','4164118250914320',6,N'Nguyễn Quang Trung','01.01.00.00',N'Ban Giám đốc',756563473,338675425,417888048,2021,12),
-- ('136','4459270549233680',6,N'Nguyễn Quang Trung','01.01.00.00',N'Ban Giám đốc',756563473,338675425,417888048,2021,9),
-- ('136','4236704639162920',6,N'Nguyễn Quang Trung','01.01.00.00',N'Ban Giám đốc',756563473,338675425,417888048,2022,1),
-- ('136','4138717804472180',6,N'Nguyễn Quang Trung','01.01.00.00',N'Ban Giám đốc',756563473,338675425,417888048,2022,2),
-- ('141','4393048250573900',6,N'Bùi Văn Mạnh','01.01.00.00',N'Ban Giám đốc',776197526,329958214,446239312,2021,10),
-- ('141','4180768873236720',6,N'Bùi Văn Mạnh','01.01.00.00',N'Ban Giám đốc',776197526,329958214,446239312,2021,11),
-- ('141','4589144158296460',6,N'Bùi Văn Mạnh','01.01.00.00',N'Ban Giám đốc',776197526,329958214,446239312,2021,12),
-- ('141','4254471830782200',6,N'Bùi Văn Mạnh','01.01.00.00',N'Ban Giám đốc',776197526,329958214,446239312,2021,9),
-- ('141','4698660525189280',6,N'Bùi Văn Mạnh','01.01.00.00',N'Ban Giám đốc',776197526,329958214,446239312,2022,1),
-- ('141','4071369213896540',6,N'Bùi Văn Mạnh','01.01.00.00',N'Ban Giám đốc',776197526,329958214,446239312,2022,2),
-- ('142','4371734054679620',7,N'Nguyễn Thị Thanh Thảo','01.01.00.00',N'Ban Giám đốc',780293438,326596181,453697257,2021,10),
-- ('142','4581192154409640',7,N'Nguyễn Thị Thanh Thảo','01.01.00.00',N'Ban Giám đốc',780293438,326596181,453697257,2021,11),
-- ('142','4674973660463290',7,N'Nguyễn Thị Thanh Thảo','01.01.00.00',N'Ban Giám đốc',780293438,326596181,453697257,2021,12),
-- ('142','4681401688269890',7,N'Nguyễn Thị Thanh Thảo','01.01.00.00',N'Ban Giám đốc',780293438,326596181,453697257,2021,9),
-- ('142','4478126871956720',7,N'Nguyễn Thị Thanh Thảo','01.01.00.00',N'Ban Giám đốc',780293438,326596181,453697257,2022,1),
-- ('142','4876393431928130',7,N'Nguyễn Thị Thanh Thảo','01.01.00.00',N'Ban Giám đốc',780293438,326596181,453697257,2022,2),
-- ('144','4537180942957500',8,N'Phan Thị Hương','01.01.00.00',N'Ban Giám đốc',777172409,333009996,444162413,2021,10),
-- ('144','4529063978527690',8,N'Phan Thị Hương','01.01.00.00',N'Ban Giám đốc',777172409,333009996,444162413,2021,11),
-- ('144','4565471491745970',8,N'Phan Thị Hương','01.01.00.00',N'Ban Giám đốc',777172409,333009996,444162413,2021,12),
-- ('144','4246275864952140',8,N'Phan Thị Hương','01.01.00.00',N'Ban Giám đốc',777172409,333009996,444162413,2021,9),
-- ('144','4987756756902310',8,N'Phan Thị Hương','01.01.00.00',N'Ban Giám đốc',777172409,333009996,444162413,2022,1),
-- ('144','4961214929069230',8,N'Phan Thị Hương','01.01.00.00',N'Ban Giám đốc',777172409,333009996,444162413,2022,2),
-- ('254','4256911423453680',15,N'Phạm Thị Thu Thủy','01.05.00.00',N'Văn phòng Công ty',492321618,172100840,320220778,2021,10),
-- ('254','4491001152677520',15,N'Phạm Thị Thu Thủy','01.05.00.00',N'Văn phòng Công ty',492321618,172100840,320220778,2021,11),
-- ('254','4564253256458750',15,N'Phạm Thị Thu Thủy','01.05.00.00',N'Văn phòng Công ty',492321618,172100840,320220778,2021,12),
-- ('254','4719102280337270',15,N'Phạm Thị Thu Thủy','01.05.00.00',N'Văn phòng Công ty',492321618,172100840,320220778,2021,9),
-- ('254','4993513249730580',15,N'Phạm Thị Thu Thủy','01.05.00.00',N'Văn phòng Công ty',492321618,172100840,320220778,2022,1),
-- ('254','4181651162004080',15,N'Phạm Thị Thu Thủy','01.05.00.00',N'Văn phòng Công ty',492321618,172100840,320220778,2022,2),
-- ('278','4921698910761370',6,N'Nguyễn Văn Thanh','01.08.00.00',N'Trung tâm Giám định Cẩm Phả',540821955,170066100,370755855,2021,10),
-- ('278','4217844153061980',6,N'Nguyễn Văn Thanh','01.08.00.00',N'Trung tâm Giám định Cẩm Phả',540821955,170066100,370755855,2021,11),
-- ('278','4039806361192190',6,N'Nguyễn Văn Thanh','01.08.00.00',N'Trung tâm Giám định Cẩm Phả',540821955,170066100,370755855,2021,12),
-- ('278','4110989751640050',6,N'Nguyễn Văn Thanh','01.08.00.00',N'Trung tâm Giám định Cẩm Phả',540821955,170066100,370755855,2021,9),
-- ('278','4300361596775130',6,N'Nguyễn Văn Thanh','01.08.00.00',N'Trung tâm Giám định Cẩm Phả',540821955,170066100,370755855,2022,1),
-- ('278','4822897756672030',6,N'Nguyễn Văn Thanh','01.08.00.00',N'Trung tâm Giám định Cẩm Phả',540821955,170066100,370755855,2022,2),
-- ('333','4460591284161710',14,N'Nguyễn Thị Tú','01.05.00.00',N'Văn phòng Công ty',539656984,193548000,346108984,2021,10),
-- ('333','4175187155796500',14,N'Nguyễn Thị Tú','01.05.00.00',N'Văn phòng Công ty',539656984,193548000,346108984,2021,11),
-- ('333','4508741179672000',14,N'Nguyễn Thị Tú','01.05.00.00',N'Văn phòng Công ty',539656984,193548000,346108984,2021,12),
-- ('333','4212413294973980',14,N'Nguyễn Thị Tú','01.05.00.00',N'Văn phòng Công ty',539656984,193548000,346108984,2021,9),
-- ('333','4981400629002130',14,N'Nguyễn Thị Tú','01.05.00.00',N'Văn phòng Công ty',539656984,193548000,346108984,2022,1),
-- ('333','4189955427549670',14,N'Nguyễn Thị Tú','01.05.00.00',N'Văn phòng Công ty',539656984,193548000,346108984,2022,2),
-- ('342','4112007170659600',10,N'Trương Nguyễn Chí Quảng','01.21.00.00',N'Công đoàn',683467540,283294948,400172592,2021,10),
-- ('342','4251284571591720',10,N'Trương Nguyễn Chí Quảng','01.21.00.00',N'Công đoàn',683467540,283294948,400172592,2021,11),
-- ('342','4520973561751760',10,N'Trương Nguyễn Chí Quảng','01.21.00.00',N'Công đoàn',683467540,283294948,400172592,2021,12),
-- ('342','4622082438165950',10,N'Trương Nguyễn Chí Quảng','01.21.00.00',N'Công đoàn',683467540,283294948,400172592,2021,9),
-- ('342','4157699351326130',10,N'Trương Nguyễn Chí Quảng','01.21.00.00',N'Công đoàn',683467540,283294948,400172592,2022,1),
-- ('342','4670872324029220',10,N'Trương Nguyễn Chí Quảng','01.21.00.00',N'Công đoàn',683467540,283294948,400172592,2022,2),
-- ('614','4841330372259880',22,N'Trần Đức Phong','01.09.00.00',N'Trung tâm Giám định Hòn Gai',214883009,83800740,131082269,2021,10),
-- ('614','4726141184272860',22,N'Trần Đức Phong','01.09.00.00',N'Trung tâm Giám định Hòn Gai',214883009,83800740,131082269,2021,11),
-- ('614','4693360608803340',22,N'Trần Đức Phong','01.09.00.00',N'Trung tâm Giám định Hòn Gai',214883009,83800740,131082269,2021,12),
-- ('614','4247789961025710',22,N'Trần Đức Phong','01.09.00.00',N'Trung tâm Giám định Hòn Gai',214883009,83800740,131082269,2021,9),
-- ('614','4199511545498000',22,N'Trần Đức Phong','01.09.00.00',N'Trung tâm Giám định Hòn Gai',214883009,83800740,131082269,2022,1),
-- ('614','4116189865060030',22,N'Trần Đức Phong','01.09.00.00',N'Trung tâm Giám định Hòn Gai',214883009,83800740,131082269,2022,2)