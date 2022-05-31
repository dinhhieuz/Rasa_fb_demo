--# Table
--## zalo_user
--    - id_user (int) <- Tăng mã tự động
--    - name
--    - birth
--    - id_zalo
--    - position
--    - gender
--    - phone
--    - email

create table zalo_user (
	id_user int,
	first_n nvarchar(20),
	last_n nvarchar(20),
	birth date,
	id_zalo nvarchar(30),
	position nvarchar(30),
	gender nvarchar(10),
	phone varchar(10),
	email varchar(50),
	department nvarchar(100)
)
Insert into zalo_user
Values 
	(1, N'Hiếu', N'Trần Đình', '2000-08-21', '8668477534363029464', N'Trùm trung bộ', 'Nam', '0123456789', 'hieudeptrai@gmail.com', N'Chuyên viên kĩ thuật'),
	(2, N'Hùng', N'Nguyễn Hữu', '1990-01-01', '5019588681863780157', N'Chủ tịch', 'Nam', '0235698563', 'hungvippro@gmail.com', N'Chủ tịch'),
	(3, N'Tổng', N'Trần Thiên Quốc', '1999-01-01', '8668477534363029464', N'Giám đốc', 'Nam', '0245896358', 'tongvippro@gmail.com', N'Giám đốc'),
	(4, N'Minh', N'Nguyễn Văn', '1999-01-01', '5853046567901647022', N'Trùm đất quảng', 'Nam', '0325698563', 'minhvippro@gmail.com', N'Bảo vệ')

--## zalo_salary
--    - id_salary (int) <- Tăng mã tự động
--    - id_user 
--    - advance (advance payment)
--    - remaining (Còn lại)
--    - total
--    - month
--    - year
--    - edit_date
--    - status (chốt lương hay chưa)

CREATE TABLE zalo_salary (
	id_salary int,
	id_user int,
	total int,
	advance int,
	remaining int,
	
	month_s int,
	year_s int,
	status nvarchar(10)
)
INSERT INTO zalo_salary (id_salary, id_user, total, advance, remaining, month_s, year_s)
VALUES
	(1, 1, 10000000, 5000000, 500000,3,2022)
--## zalo_product
--    - id_product
--    - name_p
--    - price_p
CREATE TABLE zalo_product (
	id_product int,
	name_p nvarchar(100),
	price_p int
)
INSERT INTO zalo_product
VALUES 
	(1, N'Sầu riêng', 50000),
	(2, N'Hào sản ni', 40000),
	(3, N'Sò điệp', 30000),
	(4, N'Chuối gai', 20000),
	(5, N'Dưa háo', 10000)

--## zalo_details_salary
--    - id_salary
--    - date
--    - product
--    - number
--    - price
--    - charge

CREATE TABLE zalo_details_salary (
	id_salary int,
	date_d datetime,
	id_product int,
	number int,
	charge int
)
INSERT INTO zalo_details_salary
VALUES 
	(1, '2022-03-03', 1, 100, 5000000),
	(1, '2022-03-06', 4, 100, 2000000),
	(1, '2022-03-08', 3, 100, 2000000)
--## zalo_salary_send
--    - id_send (int) <- Tăng mã tự động
--    - id_zalo
--    - time_send
--    - status
CREATE TABLE zalo_salary_send (
	id_send int,
	id_zalo nvarchar(50),
	id_salary int,
	time_send datetime,
	status nvarchar(50)
)
INSERT INTO zalo_salary_send
VALUES
	(1, '8668477534363029464', 1, '2022-03-31', 'send success')

--# Procedure
--    - Create (zalo_user)
exec proc_all N'authorized', NULL, NULL, NULL, N'4857932260991004'
--    - Create (Tạo lương tự động)
alter PROCEDURE zalo_create_salary (
	@user_zalo nvarchar(50)
)
AS 
BEGIN 
	if (select count(id_user) from zalo_user where id_zalo = @user_zalo) = 1
	begin
		if (select count(id_salary)
				from (
					select l.id_salary, id_user, id_send, id_zalo, time_send, l.status 
					from zalo_salary l left join zalo_salary_send s ON l.id_salary = s.id_salary
				) as B 
			WHERE id_user = (select id_user from zalo_user where id_zalo = @user_zalo) and id_send is null) = 0
		BEGIN
			declare @id_salary int = (select max(id_salary) + 1 from zalo_salary)
			declare @dem smallint = 0
			declare @today datetime = getdate()
			
			WHILE @dem < 4
			BEGIN
				------> TẠO BẢN zalo_details_salary TỰ ĐỘNG
				DECLARE @number_p int = round((rand()*(100-1+1)+1),0) --rand 1 >= X <= 100

				INSERT zalo_details_salary (id_salary, date_d, id_product, number, charge)
				SELECT TOP 1 
					@id_salary, 
					DATEFROMPARTS(YEAR(@today),MONTH(@today), ROUND((RAND()*(28-1)+1),0)), 
					id_product, 
					@number_p,
					(@number_p*price_p)
				FROM zalo_product ORDER BY NEWID()

				------------
				set @dem = @dem + 1
			END
			------> TẠO BẢN zalo_salary ,
			DECLARE @total int = (SELECT SUM(charge) FROM zalo_details_salary WHERE id_salary = @id_salary)
			DECLARE @advance int = Round(rand()*(@total-10000)+10000,0)

			INSERT INTO zalo_salary(id_salary, id_user, total, advance, remaining, month_s, year_s, status)
			SELECT 
				@id_salary
				, (select id_user from zalo_user where id_zalo = @user_zalo)
				, @total, @advance, (@total - @advance)
				, MONTH(@today), YEAR(@today), 'done'
		END 
		else
			print(N'Đã có lương chưa được gửi')
	end
	else
		print(N'Không tồn tại tài khoản')
	-- EXEC zalo_create_salary '8668477534363029464'
	-- EXEC zalo_create_salary '2240115057973899906'
END
					-- Select * from zalo_user
					-- select * from zalo_salary 
						--update zalo_salary
						--set status = 'done'
						--where id_salary = 2
					 delete from zalo_salary
					 where id_salary = 2
					 delete from zalo_details_salary
					 where id_salary = 2
					-- select * from zalo_link_fb
					-- select * from zalo_details_salary
					-- select * from zalo_salary_send
					-- select * from zalo_product

ALTER TRIGGER trig_zalo_send_auto
ON dbo.zalo_salary
FOR INSERT, UPDATE
AS
BEGIN
	-- Lương chốt thì sẽ gửi đi cho nhân viên
	
	IF (select count(l.id_salary) 
		from zalo_salary l left join zalo_salary_send s ON l.id_salary = s.id_salary 
		where id_send is NULL and l.status = 'done') > 0 
	BEGIN
		--DECLARE @INPUT_DATA nvarchar(3999) = '
		--	select 
		--		 l.id_user, UPPER(concat(last_n, '' '', first_n)) as name_u, FORMAT(birth, ''dd/MM/yyyy'') as birth, position, u.id_zalo
		--		 , l.id_salary, month_s, year_s
		--		 , d.id_product, p.name_p, convert(date,d.date_d) as date_d, p.price_p, d.number, d.charge , total, advance, remaining
		--	from 
		--		zalo_details_salary d left join zalo_salary l ON l.id_salary = d.id_salary
		--					  left join zalo_salary_send s ON l.id_salary = s.id_salary 
		--					  left join zalo_user u ON l.id_user = u.id_user
		--					  left join zalo_product p ON d.id_product = p.id_product
		--	where 
		--		id_send is NULL 
		--		and l.status = ''done'' '
		DECLARE @INPUT_DATA nvarchar(3999) = '
			select 
				 l.id_user, UPPER(concat(last_n, '' '', first_n)) as name_u, FORMAT(birth, ''dd/MM/yyyy'') as birth, position, u.id_zalo
				 , l.id_salary, month_s, year_s
				 , d.id_product, p.name_p, convert(date,d.date_d) as date_d
				 , LEFT(FORMAT( p.price_p, ''N'', ''vi-VN''), (LEN(FORMAT( p.price_p, ''N'', ''vi-VN''))-3)) AS price_p
				 , LEFT(FORMAT( d.number, ''N'', ''vi-VN''), (LEN(FORMAT( d.number, ''N'', ''vi-VN''))-3)) AS number
				 , LEFT(FORMAT( d.charge, ''N'', ''vi-VN''), (LEN(FORMAT( d.charge, ''N'', ''vi-VN''))-3)) AS charge
				 , LEFT(FORMAT( total, ''N'', ''vi-VN''), (LEN(FORMAT( total, ''N'', ''vi-VN''))-3)) AS total
				 , LEFT(FORMAT( advance, ''N'', ''vi-VN''), (LEN(FORMAT( advance, ''N'', ''vi-VN''))-3)) AS advance
				 , LEFT(FORMAT( remaining, ''N'', ''vi-VN''), (LEN(FORMAT( remaining, ''N'', ''vi-VN''))-3)) AS remaining
			from 
				zalo_details_salary d left join zalo_salary l ON l.id_salary = d.id_salary
							  left join zalo_salary_send s ON l.id_salary = s.id_salary 
							  left join zalo_user u ON l.id_user = u.id_user
							  left join zalo_product p ON d.id_product = p.id_product
			where 
				id_send is NULL 
				and l.status = ''done'' '
		EXECUTE (@INPUT_DATA)
		--Tạo bảng ảo lưu kết quả
		DECLARE @RESULT_POST TABLE (
			id_salary int,
			id_send int,
			id_zalo nvarchar(50),
			status nvarchar(50),
			time_send datetime
		)

		-- Sending to people of list by Python
		INSERT INTO @RESULT_POST EXECUTE sp_execute_external_script @language = N'Python'
			, @script = N'
#------------------------(NOTE) TẠO BẢNG KẾT QUẢ GỬI CHO NHANH VIÊN 
import numpy as np #-> ver: 1.19.5
import six #-> ver: 1.15.0
import matplotlib.pyplot as plt #-> ver: 3.3.4
import pandas as pd #-> ver: 1.3.5

#----CREATE IMAGE
def table(df = None, name_img = None, title = ""):  
    try:
        #----- Set column STT from Index
        df.index = np.arange(1, len(df) + 1)
        df = df.rename_axis("STT").reset_index()

        def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                            header_color="#40466e", row_colors=["#f1f1f2", "w"], edge_color="w",
                            bbox=[0, 0, 1, 1], header_columns=0,
                            ax=None, **kwargs):
            if ax is None:
                size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
                fig, ax = plt.subplots(figsize=size)
                #Title of table
                ax.set_title(title, fontdict={"fontsize":18, "fontweight":28,"verticalalignment": "baseline"})
                ax.axis("off")
            ax.axis([0,1,data.shape[0],-1]) ## <---------- Change here
            #---Param: Title table
            mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
            mpl_table.auto_set_font_size(False)
            mpl_table.set_fontsize(font_size)
            mpl_table.auto_set_column_width(col=list(range(len(df.columns))))

            for k, cell in six.iteritems(mpl_table._cells):
                cell.set_edgecolor(edge_color)
                if k[0] == 0 or k[1] < header_columns:
                    cell.set_text_props(weight="bold", color="w")
                    cell.set_facecolor(header_color)
                else:
                    cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
            return ax

        def set_row_edge_color(ax, row, column, color):
            #--Grid Row in the table
            for x in range(-1, row+1): ax.axhline(x, color=color)
            #--Grib Column in the table
            # for y in range(column+1): ax.axvline(y/column, color=color)
            for y in range(column): ax.axvline(y, color=color)

        ax = render_mpl_table(df, header_columns=0, col_width=2.0)
        set_row_edge_color(ax, df.shape[0], df.shape[1], "k")
        # Export Styled Table to PNG
        #---File đang đứng ở chatbot_demo
        
        plt.savefig(name_img, format="png", bbox_inches="tight",dpi = 80)
#         plt.show()

        return 1
    except:
        return 0

#-------------------------------------------
db = InputDataSet
df_check = []

#Dữ liệu bảng lương
user = db[["id_user", "name_u", "birth", "position", "id_zalo", "month_s", "year_s", "total", "advance", "remaining"]].drop_duplicates().reset_index()
salary = db[["id_salary", "id_user", "id_product", "name_p", "date_d", "price_p", "number", "charge"]]
salary.rename(index=str,columns={"id_salary":"Mã lương", "id_user":"Mã NV", "id_product":"Mã SP", "name_p":"Tên SP", "date_d":"Ngày làm", "price_p":"Giá SP", "number":"Số lượng", "charge":"Thành tiền"},inplace=True)

from datetime import datetime
# chạy từng user

for i in range(len(user)):
    time = datetime.now()
    # Thông tin bảng lương
    # title = "BẢNG LƯƠNG THÁNG {0} NĂM {1}".format(user["month_s"], user["year_s"])
    title = "BẢNG LƯƠNG THÁNG {0} NĂM {1} (Tên: {2} - Chức vụ: {3})".format(user["month_s"][i], user["year_s"][i], user["name_u"][i], user["position"][i])
    name_img = "img.png"
    df = salary.loc[salary["Mã NV"]==user["id_user"][i]]
    check = table(df = df[["Mã lương", "Tên SP", "Ngày làm", "Giá SP", "Số lượng", "Thành tiền"]], name_img = name_img, title = title)
    if check == 1:
        #-----------------UPLOAD IMAGE TO SERVER ZALO
        import requests
        import json
        url = "https://openapi.zalo.me/v2.0/oa/upload/image"
        files = [
          ("file",("file",open(name_img,"rb"),"multipart/form-data"))
        ]
        access_token = "n015SAB27KB90KPqhy0SHia8JdEWrc86itHdRxxCE5gMU1iDWiz4GRvy5moqkWXTXojLFUcQS0tdBs5Eq8zpURSBIp2HhX9Qh3KyQ9JoOGQmO4XDbzbiBOP-QcJWnMCd-Gn04P3AVdgXJ5Sfkyjk5D1yCbJu_1GawZKJGiMW3JMlAYjJdhaK3uOSE7gwks8hZX5T5xwPO5wu87XfihnmMTmeNYsrWdfTeZrQQ96P10dwFoLvnVy0DhPvHdYdtcSQY7ivMwJJ46YSRmCrhAq71AeJEKsOcHW7yGeWMlUh2JUGF39bk8Pf3vCvMtY9XK8xlIKGPvES41Bv8q9ESNDUy6i4hjuVJ0"
        headers = { "access_token": access_token }

        response = requests.request("POST", url, headers = headers, files=files)
        #---------------SEND IMAGE TO USER
        if response.ok:
            end_point = "https://openapi.zalo.me/v2.0/oa/message"
            user_id = user["id_zalo"][i]
            text = "BẢNG LƯƠNG CỦA THÁNG {0} NĂM {1}\n ---------\n   - Tên: {2} (Mã nv: {3})\n   - Ngày Sinh: {4}\n   - Chức vụ: {5}\n ---------\n Tổng lương: {6}\n Ứng trước: {7}\n Còn lại: {8}".format(user["month_s"][i], user["year_s"][i], user["name_u"][i], user["id_user"][i], user["birth"][i], user["position"][i], user["total"][i], user["advance"][i], user["remaining"][i])
            payload = { 
              "recipient": {
                "user_id": user_id
              },
              "message": {
                "text": text,
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "media",
                        "elements": [{
                            "media_type": "image",
                            "attachment_id": response.json()["data"].get("attachment_id"),
            #                 "url": "https://interactive-examples.mdn.mozilla.net/media/cc0-images/grapefruit-slice-332-332.jpg"
                        }]
                    }
                }
              }
            }
            response = requests.post(end_point, data=json.dumps(payload), headers = headers)
            if response.ok:
                status = "send success"
            else: 
                status = "send failed"
        else: 
            status = "upload image failed"
    else: 
        status = "create image failed"   
    df_check.append({"id_send":i, "id_zalo": user["id_zalo"][i], "id_salary": df["Mã lương"][0], "time_send": time, "status": status})
OutputDataSet = pd.DataFrame.from_dict(df_check, orient="columns")
			'
			, @input_data_1 = @INPUT_DATA;

		--> Lưu kết quả log lại cho người dùng
		SELECT * FROM @RESULT_POST
		DECLARE @id_send int = (select max(id_send) from zalo_salary_send)
		print(1)
		INSERT INTO dbo.zalo_salary_send 
			SELECT (id_send + @id_send), id_zalo, id_salary, time_send, status FROM @RESULT_POST
	END
END

-- BẢNG LIÊN KẾT ZALO và FACEBOOK
--CREATE TABLE zalo_link_fb (
--	id_zalo nvarchar(50),
--	id_fb nvarchar(50),
--)
INSERT INTO zalo_link_fb
VALUES
	('5019588681863780157', '5108783099144657')
	update zalo_link_fb
	set id_zalo = '2240115057973899906'
	where id_fb = '5108783099144657'
select * from zalo_user 

select * from zalo_link_fb
insert into users
values
	(5, '5108783099144657', N'Trần Thiên Quốc', N'Tổng', 'full_control')
----- TẠO THỦ TỤC TẠO TRONG RASA
--ALTER PROCEDURE proc_create_user_at_fb (
--	@id_fb nvarchar(50)
--) as
--BEGIN
--	IF(SELECT COUNT(id_zalo) FROM zalo_link_fb WHERE id_fb = @id_fb) > 0
--	BEGIN
--		DECLARE @zalo nvarchar(50) = (SELECT id_zalo FROM zalo_link_fb WHERE id_fb = @id_fb)
--		EXEC zalo_create_salary @zalo
--	END
--END

--exec proc_create_user_at_fb '4857932260991004'


---> CREATE FUNCTION
Declare @Number int = 111111111
SELECT FORMAT( @Number, 'N', 'vi-VN')  AS 'VN Number Format'

select 
				 l.id_user, UPPER(concat(last_n, ' ', first_n)) as name_u, FORMAT(birth, 'dd/MM/yyyy') as birth, position, u.id_zalo
				 , l.id_salary, month_s, year_s
				 , d.id_product, p.name_p, convert(date,d.date_d) as date_d
				 , LEFT(FORMAT( p.price_p, 'N', 'vi-VN'), (LEN(FORMAT( p.price_p, 'N', 'vi-VN'))-3)) AS price_p
				 , LEFT(FORMAT( d.number, 'N', 'vi-VN'), (LEN(FORMAT( d.number, 'N', 'vi-VN'))-3)) AS number
				 , LEFT(FORMAT( d.charge, 'N', 'vi-VN'), (LEN(FORMAT( d.charge, 'N', 'vi-VN'))-3)) AS charge
				 , LEFT(FORMAT( total, 'N', 'vi-VN'), (LEN(FORMAT( total, 'N', 'vi-VN'))-3)) AS total
				 , LEFT(FORMAT( advance, 'N', 'vi-VN'), (LEN(FORMAT( advance, 'N', 'vi-VN'))-3)) AS advance
				 , LEFT(FORMAT( remaining, 'N', 'vi-VN'), (LEN(FORMAT( remaining, 'N', 'vi-VN'))-3)) AS remaining
			from 
				zalo_details_salary d left join zalo_salary l ON l.id_salary = d.id_salary
							  left join zalo_salary_send s ON l.id_salary = s.id_salary 
							  left join zalo_user u ON l.id_user = u.id_user
							  left join zalo_product p ON d.id_product = p.id_product
			where 
				id_send is NULL 
				and l.status = 'done'