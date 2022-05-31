(Nhân viên)
Họ và tên (f_name, l_name)
Chức danh (position)
Mã nhân viên (id_nv)
Phòng ban (department)

(Bảng lương)
Mã lương (id_l)
Mã nhân viên (id_nv)
Ngày lương (ngay_l)
Tổng thu nhập (total)
Mức lương đóng BHXH (t_mldBHXH)
Phụ cấp trách nhiệm (t_pctn)
Hệ 
Các khoản giảm trừ (reduce)
Còn lại thực nhận (residual)

Tổng mức bảo hiểm công ty đóng cho NLĐ (insurance)

--> CREATE TABLE 
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
	(3, N'Tổng', N'Trần Thiên Quốc', '1999-01-01', '2240115057973899906', N'Giám đốc', 'Nam', '0245896358', 'tongvippro@gmail.com', N'Giám đốc'),
	(4, N'Minh', N'Nguyễn Văn', '1999-01-01', '5853046567901647022', N'Trùm đất quảng', 'Nam', '0325698563', 'minhvippro@gmail.com', N'Bảo vệ')

create TABLE zalo_luong (
    id_l int,
    id_nv int,
    date_l date,
    total int,
    t_lc int,
    t_lnp int,
    t_lnl int,
    t_lncd int,
    t_lng int,
    t_lcd int,
    t_lcl int,
    t_pvtad smallint,
    t_tcldnccn smallint,
    t_tl smallint,
    t_others int,
    t_htdt int,
    t_htxx int,
    t_htdl int,
    t_htno int,
    t_pcbskxd int,
    t_tagc int,
    t_cn smallint,
    t_pcnn smallint,
    t_lpcdBHXH int,
    t_pcbskxdkn int,
    t_kpidv float,
    t_cc smallint,
    t_nl smallint,
    t_ng smallint,
    t_cl smallint,
    t_mldBHXH int,
    t_pctn int,
    t_hsPCBS_KXĐ float,
    t_htt varchar(10),
    t_hsdv smallint,
    t_np smallint,
    t_ncd smallint,
    t_cd smallint,
    decline int,
    d_tuk1 int,
    d_cdp int,
    d_bhxh int,
    d_bhyt int,
    d_bhtn int,
    d_ttncn int,
    d_ttbhsknt smallint,
    d_bt smallint,
    d_tt smallint,
	insurance int, 
    i_bhxh int,
    i_bhyt int,
    i_bhtn int,
	residual int,
	status varchar(10)
)

-------------DATA CREATING PROCEDURE -------------
CREATE PROCEDURE proc_chatbot_create_luong_cang (
	@id_fb varchar(100),
	@status varchar(100)
) AS
BEGIN
	
	--(Mã lương tăng dần)
	DECLARE @id_l int = (SELECT IIF(MAX(id_l) is null,1, MAX(id_l)+1) from zalo_luong)
	--(thêm dữ liệu bảng lương)
	Insert into zalo_luong 
	SELECT 
		@id_l as id_l, 
		(select id_user from zalo_user where id_zalo = (SELECT id_zalo FROM zalo_link_fb WHERE id_fb = @id_fb)) as id_nv, 
		CONVERT(DATE, GETDATE()) as date_l,
		0 as total,
		round(rand()*(50-10+10)+10,3)*1000000 as t_lc,
		round(rand(),3)*1000000 as t_lnp,
		Round(rand(),3)*1000000 as t_lnl,
		0 as t_lncd,
		0 as t_lng,
		0 as t_lcd,
		Round(rand(),3)*1000000 as t_lcl,
		0 as t_pvtad,
		0 as t_tcldnccn,
		0 as t_tl,
		0 as t_others,
		Round(rand(),2)*1000000 as t_htdt,
		Round(rand(),2)*1000000 as t_htxx,
		Round(rand(),2)*1000000 as t_htdl,
		Round(rand(),2)*1000000 as t_htno,
		Round(rand(),2)*1000000 as t_pcbskxd,
		Round(rand(),2)*1000000 as t_tagc,
		0 as t_cn,
		0 as t_pcnn,
		5000000 as t_lpcdBHXH,
		0 as t_pcbskxdkn,
		Round(rand()*(10-3+3),1) as t_kpidv,
		Round(rand(),0)*10 t_cc,
		Round(rand()*(6),0) as t_nl,
		Round(rand()*(6),0) as t_ng,
		Round(rand()*(6),0) as t_cl,
		5000000 as t_mldBHXH,
		0 as t_pctn,
		Round(rand()*(10-3+3),1) as t_hsPCBS_KXĐ,
		substring('ABCDEF', (abs(checksum(newid())) % 6)+1, 1) as t_htt,
		Round(rand(),0)*4 as t_hsdv,
		0 as t_np,
		0 as t_ncd,
		0 as t_cd,
		NULL as decline,
		Round(rand(),3)*1000000 as d_tuk1,
		Round(rand(),3)*100000 as d_cdp,
		Round(rand(),3)*100000 as d_bhxh,
		Round(rand(),3)*100000 as d_bhyt,
		Round(rand(),3)*100000 as d_bhtn,
		Round(rand(),3)*100000 as d_ttncn,
		0 as d_ttbhsknt,
		0 as d_bt,
		0 as d_tt,
		0 as insurance,
		Round(rand(),3)*100000 as i_bhxh,
		Round(rand(),3)*100000 as i_bhyt,
		Round(rand(),3)*100000 as i_bhtn,
		0 as residual,
		@status as status

	--Tính tổng, trừ, bảo hiểm, còn lại
	declare @total int, @decline int, @residual int, @insurance int

	select @total = (t_lc + t_lnp + t_lnl + t_lncd + t_lng + t_lcd + 
				t_lcl + t_pvtad + t_tcldnccn + t_tl + t_others + 
				t_htdl + t_htxx + t_htdl + t_htno + t_pcbskxd + 
				t_tagc + t_cn + t_pcnn + t_lpcdBHXH),
		   @decline = (d_tuk1 + d_cdp + d_bhxh + d_bhyt + d_bhtn + d_ttncn + d_ttbhsknt + d_bt + d_tt ),
		   @insurance = (i_bhtn + i_bhxh + i_bhtn)
	from zalo_luong 
	WHERE 
		id_l = @id_l
	SET @residual = @total - @decline - @insurance

	-- Cập nhật thông tin bảng lương
	UPDATE zalo_luong
	SET total = @total,
		decline = @decline,
		insurance = @insurance,
		residual = @residual
	WHERE 
		id_l = @id_l

	--	TEST
--		EXEC proc_chatbot_create_luong_cang '4857932260991004', 'done'
--		delete from zalo_luong
--		select * from zalo_luong
end

------------------------ TRIGGER TO SEND TABLE
ALTER TRIGGER trig_send_salary_zalo_final
ON dbo.zalo_luong
FOR UPDATE, INSERT
AS
BEGIN
	if (SELECT count(l.id_l) FROM zalo_luong l 
			left join zalo_user u ON l.id_l = u.id_user
			left join zalo_salary_send s ON l.id_l = s.id_salary 
		WHERE l.status = 'done' AND s.status is null) > 0 
	BEGIN
		
		DECLARE @input_data nvarchar(max) = N'SELECT 
			CONCAT(u.last_n,'' '',u.first_n) as name_u, 
			IIF(gender = ''nam'', ''Anh'', N''Chị'') as gender,
			position, department,[id_nv], u.id_zalo, l.id_l, l.date_l
			, LEFT(FORMAT( [total] , ''N'', ''vi-VN''), (LEN(FORMAT( [total] , ''N'', ''vi-VN''))-3)) AS [total] 
			, LEFT(FORMAT( [t_lc] , ''N'', ''vi-VN''), (LEN(FORMAT( [t_lc] , ''N'', ''vi-VN''))-3)) AS [t_lc]
			, LEFT(FORMAT( [t_lnp] , ''N'', ''vi-VN''), (LEN(FORMAT( [t_lnp] , ''N'', ''vi-VN''))-3)) AS [t_lnp]
			, LEFT(FORMAT( [t_lnl] , ''N'', ''vi-VN''), (LEN(FORMAT( [t_lnl] , ''N'', ''vi-VN''))-3)) AS [t_lnl]
			,[t_lncd],[t_lng],[t_lcd]
			, LEFT(FORMAT( [t_lcl] , ''N'', ''vi-VN''), (LEN(FORMAT( [t_lcl] , ''N'', ''vi-VN''))-3)) AS [t_lcl]
			,[t_pvtad],[t_tcldnccn]
			,[t_tl],[t_others]
			, LEFT(FORMAT( [t_htdt] , ''N'', ''vi-VN''), (LEN(FORMAT( [t_htdt] , ''N'', ''vi-VN''))-3)) AS [t_htdt]
			, LEFT(FORMAT( [t_htxx] , ''N'', ''vi-VN''), (LEN(FORMAT( [t_htxx] , ''N'', ''vi-VN''))-3)) AS [t_htxx]
			, LEFT(FORMAT( [t_htdl] , ''N'', ''vi-VN''), (LEN(FORMAT( [t_htdl] , ''N'', ''vi-VN''))-3)) AS [t_htdl]
			, LEFT(FORMAT( [t_htno] , ''N'', ''vi-VN''), (LEN(FORMAT( [t_htno] , ''N'', ''vi-VN''))-3)) AS [t_htno]
			, LEFT(FORMAT( [t_pcbskxd] , ''N'', ''vi-VN''), (LEN(FORMAT( [t_pcbskxd] , ''N'', ''vi-VN''))-3)) AS [t_pcbskxd]
			, LEFT(FORMAT( [t_tagc] , ''N'', ''vi-VN''), (LEN(FORMAT( [total] , ''N'', ''vi-VN''))-3)) AS [t_tagc]
			,[t_cn],[t_pcnn]
			, LEFT(FORMAT( [t_lpcdBHXH] , ''N'', ''vi-VN''), (LEN(FORMAT( [t_lpcdBHXH] , ''N'', ''vi-VN''))-3)) AS [t_lpcdBHXH]
			,[t_pcbskxdkn],[t_kpidv],[t_cc],[t_nl],[t_ng],[t_cl]
			, LEFT(FORMAT( [t_mldBHXH] , ''N'', ''vi-VN''), (LEN(FORMAT( [t_mldBHXH] , ''N'', ''vi-VN''))-3)) AS [t_mldBHXH]
			,[t_pctn],[t_hsPCBS_KXĐ],[t_htt],[t_hsdv],[t_np],[t_ncd],[t_cd]
			, LEFT(FORMAT( [decline] , ''N'', ''vi-VN''), (LEN(FORMAT( [decline] , ''N'', ''vi-VN''))-3)) AS [decline]
			, LEFT(FORMAT( [d_tuk1] , ''N'', ''vi-VN''), (LEN(FORMAT( [d_tuk1] , ''N'', ''vi-VN''))-3)) AS [d_tuk1]
			, LEFT(FORMAT( [d_cdp] , ''N'', ''vi-VN''), (LEN(FORMAT( [d_cdp] , ''N'', ''vi-VN''))-3)) AS [d_cdp]
			, LEFT(FORMAT( [d_bhxh] , ''N'', ''vi-VN''), (LEN(FORMAT( [d_bhxh] , ''N'', ''vi-VN''))-3)) AS [d_bhxh]
			, LEFT(FORMAT( [d_bhyt] , ''N'', ''vi-VN''), (LEN(FORMAT( [d_bhyt] , ''N'', ''vi-VN''))-3)) AS [d_bhyt]
			, LEFT(FORMAT( [d_bhtn] , ''N'', ''vi-VN''), (LEN(FORMAT( [d_bhtn] , ''N'', ''vi-VN''))-3)) AS [d_bhtn]
			, LEFT(FORMAT( [d_ttncn] , ''N'', ''vi-VN''), (LEN(FORMAT( [d_ttncn] , ''N'', ''vi-VN''))-3)) AS [d_ttncn]
			,[d_ttbhsknt],[d_bt],[d_tt]
			, LEFT(FORMAT( [insurance] , ''N'', ''vi-VN''), (LEN(FORMAT( [insurance] , ''N'', ''vi-VN''))-3)) AS [insurance]
			, LEFT(FORMAT( [i_bhxh] , ''N'', ''vi-VN''), (LEN(FORMAT( [i_bhxh] , ''N'', ''vi-VN''))-3)) AS [i_bhxh]
			, LEFT(FORMAT( [i_bhyt] , ''N'', ''vi-VN''), (LEN(FORMAT( [i_bhyt] , ''N'', ''vi-VN''))-3)) AS [i_bhyt]
			, LEFT(FORMAT( [i_bhtn] , ''N'', ''vi-VN''), (LEN(FORMAT( [i_bhtn] , ''N'', ''vi-VN''))-3)) AS [i_bhtn]
			, LEFT(FORMAT( [residual] , ''N'', ''vi-VN''), (LEN(FORMAT( [residual] , ''N'', ''vi-VN''))-3)) AS [residual]
			,l.status
			,s.status as status_send
		FROM zalo_luong l 
				left join zalo_user u ON l.id_l = u.id_user
				left join zalo_salary_send s ON l.id_l = s.id_salary 
		WHERE 
			l.status = ''done''
			AND 
			s.status is null' 

		--print(@input_data)
		--EXECUTE (@input_data)
		--Tạo bảng ảo lưu kết quả
		DECLARE @RESULT_POST TABLE (
			id_salary int,
			id_send int,
			id_zalo nvarchar(50),
			status nvarchar(50),
			time_send datetime
		)
		-- INSTALL PACKGAKE HTML2IMAGE -------------------
--		EXECUTE sp_execute_external_script @language = N'Python'
--			, @script = N'
--#------------------------(NOTE) TẠO BẢNG KẾT QUẢ GỬI CHO NHANH VIÊN 
--html = ""
--html += ''<h1 style="background-color: brown;">Hieu1</h1>''
--from html2image import Html2Image
--hti = Html2Image()
--with open("index.html", "w") as outputfile:
--	outputfile.write(html)
--	hti.screenshot(outputfile, save_as="out.png")

--from os import walk
--filenames = next(walk("./"), (None, None, []))[2]
--print(filenames)
--'
	EXECUTE sp_execute_external_script @language = N'Python'
			, @script = N'
#------------------------(NOTE) TẠO BẢNG KẾT QUẢ GỬI CHO NHANH VIÊN 
import requests

HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
HCTI_API_USER_ID = "85884ef4-6b15-42d9-8351-7b672b9ffbd5"
HCTI_API_KEY = "432096bd-43dd-4c4c-9e77-69e0530154a5"

data = { "html": "<div class=''box''>Hello, world!</div>",
         "css": ".box { color: white; background-color: #0f79b9; padding: 10px; font-family: Roboto }"}

image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

print(image.json()["url"])
'
		-------------------------------------------------
		-- Sending to people of list by Python
		INSERT INTO @RESULT_POST EXECUTE sp_execute_external_script @language = N'Python'
			, @script = N'
#------------------------(NOTE) TẠO BẢNG KẾT QUẢ GỬI CHO NHANH VIÊN 
from html2image import Html2Image
import pandas as pd
from datetime import datetime


df = InputDataSet
df_check = []
for i in range(len(df)):
    month = df["date_l"][0].month
    year = df["date_l"][0].year
    html = f"""
    <div>
        <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>img{{display: block; margin-right: auto; width:29%; height:8%}}</style>
            </head><body><img src="data:image/png;base64,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" alt="image001 (1)" style="max-width:100%;"></body>
    </div>

    <!-- HEADER -->

    <center class="header" >
        <h1>CÔNG TY CỔ PHẦN CẢNG ĐÀ NẴNG </h1> 
        <h1> PHÒNG TỔ CHỨC TIỀN LƯƠNG</h1>
        <i><p style="font-size: 222%; line-height: 1.5;">Kính gửi: {df["gender"][0]} {df["name_u"][0]}</p></i>
        <h1>BẢNG LƯƠNG CHI TIẾT THÁNG {month} NĂM {year}</h1>
    </center>
    <br><br><br>

    <!-- Info employees -->
    <div class="col-wrap">
        <div class="col" style="color:white;">-----------------</div>
        <div class="col">
            <u><h3>Họ và tên:</h3></u>
            <u><h3>Chức danh: </h3></u>
        </div>
    
        <div class="col" id="values">
        <h3>{df["name_u"][0]}</h3>
        <h3>{df["position"][0]}</h3>
        </div>
    
        <div class="col">
            <u><h3>Mã nhân viên:</h3></u>
            <u><h3>Phòng ban:</h3></u>
        </div>

        <div class="col" id="values">
            <h3>{df["id_nv"][0]}</h3>
            <h3>Phòng {df["department"][0]}</h3>
        </div>
        <div class="col" style="color:white;">-----------------</div>
    </div>


    <!-- CONTENT TABLE -->
    <table class = "content" style="width:85%"  cellpadding="9">
        <caption style="caption-side: bottom; font-style: italic; text-align: right;">(Đơn vị tính: đồng)</caption>
        <thead >
            <tr>
                <td>Mức lương đóng BHXH</td> <td>{df["t_mldBHXH"][0]}</td>
                <td>PC nặng nhọc, độc hại</td> <td>{df["t_pcnn"][0]}</td>
            </tr>
            <tr>
                <td>Phụ cấp trách nhiệm</td> <td>{df["t_pctn"][0]}</td>
                <td>Lương và PC đóng BHXH</td> <td>{df["t_lpcdBHXH"][0]}</td>
            </tr>
            <tr>
                <td>Hệ số PCBS KXĐ</td> <td>{df["t_hsPCBS_KXĐ"][0]}</td>
                <td>PCBS KXĐ kiêm nhiệm</td> <td>{df["t_pcbskxdkn"][0]}</td>
            </tr>
            <tr>
                <td>Hạng thành tích</td> <td>{df["t_htt"][0]}</td>
                <td>KPI đơn vị</td> <td>{df["t_kpidv"][0]}</td>
            </tr>
            <tr>
                <td>Hệ số đơn vị</td> <td>{df["t_hsdv"][0]}</td>
                <td>Công chính</td> <td>{df["t_cc"][0]}</td>
            </tr>
            <tr>
                <td>Nghỉ phép</td> <td>{df["t_np"][0]}</td>
                <td>Nghỉ lễ, tết</td> <td>{df["t_nl"][0]}</td>
            </tr>
            <tr>
                <td>Nghỉ chế độ</td> <td>{df["t_ncd"][0]}</td>
                <td>Ngoài giờ</td> <td>{df["t_ng"][0]}</td>
            </tr>
            <tr>
                <td>Ca đêm</td> <td>{df["t_cd"][0]}</td>
                <td>Cách ly</td> <td>{df["t_cl"][0]}</td>
            </tr>
            <!-------TỔNG LƯƠNG VÀ KHOẢN TRỪ----->
            <tr>
                <th style="background-color: #83ccab;">Tổng thu nhập</th>
                <th style="background-color: #83ccab;">{df["total"][0]}</th>
                <th style="background-color: #f2b69b;">Các khoản giảm trừ</th>
                <th style="background-color: #f2b69b;">{df["decline"][0]}</th>
            </tr>
            <!------------>
            <tr>
                <td><b>Lương</b></td> <td></td>
                <td>Tạm ứng kỳ 1</td> <td>{df["d_tuk1"][0]} </td>
            </tr>
            <tr>
                <td>Lương chính</td> <td>{df["t_lc"][0]}</td>
                <td>Công đoàn phí</td> <td>{df["d_cdp"][0]}</td>
            </tr>
            <tr>
                <td>Lương nghỉ phép</td> <td>{df["t_lnp"][0]}</td>
                <td>Bảo hiểm xã hội (8%)</td> <td>{df["d_bhxh"][0]}</td>
            </tr>
            <tr>
                <td>Lương nghỉ lễ, tết</td> <td>{df["t_lnl"][0]}</td>
                <td>Bảo hiểm y tế (1,5%)</td> <td>{df["d_bhyt"][0]}</td>
            </tr>
            <tr>
                <td>Lương nghỉ chế độ</td> <td>{df["t_lncd"][0]}</td>
                <td>Bảo hiểm thất nghiệp (1%)</td> <td>{df["d_bhtn"][0]}</td>
            </tr>
            <tr>
                <td>Lương ngoài giờ</td> <td>{df["t_lng"][0]}</td>
                <td>Thuế thu nhập cá nhân</td> <td>{df["d_ttncn"][0]}</td>
            </tr>
            <tr>
                <td>Lương ca đêm</td> <td>{df["t_lcd"][0]}</td>
                <td>Thu tiền BHSK người thân</td> <td>{df["d_ttbhsknt"][0]}</td>
            </tr>
            <tr>
                <td>Lương cách ly</td> <td>{df["t_lcl"][0]}</td>
                <td>Bồi thường</td> <td>{df["d_bt"][0]}</td>
            </tr>
            <tr>
                <td>Phục vụ tàu Ấn Độ</td> <td>{df["t_pvtad"][0]}</td>
                <td>Truy thu</td> <td>{df["d_tt"][0]}</td>
            </tr>
            <tr>
                <td>TC LĐ nữ có con nhỏ</td> <td>{df["t_tcldnccn"][0]}</td>
                <td></td> <td></td>
            </tr>
            <tr>
                <td>Truy lĩnh</td> <td>{df["t_tl"][0]}</td>
                <td></td> <td></td>
            </tr>
            <tr>
                <td>Khác (Họp)</td> <td>{df["t_others"][0]}</td>
                <td></td> <td></td>
            </tr>
            <tr>
                <td><b>Hỗ trợ & bổ sung không xác định</b></td> <td></td>
                <td></td> <td></td>
            </tr>
            <tr>
                <td>Hỗ trợ Điện thoại</td> <td>{df["t_htdt"][0]}</td>
                <td></td> <td></td>
            </tr>
            <tr>
                <td>Hỗ trợ Xăng xe</td> <td>{df["t_htxx"][0]}</td>
                <td></td> <td></td>
            </tr>
            <tr>
                <td>Hỗ trợ Đi lại</td> <td>{df["t_htdl"][0]}</td>
                <td></td> <td></td>
            </tr>
            <tr>
                <td>Hỗ trợ Nhà ở</td> <td>{df["t_htno"][0]}</td>
                <td></td> <td></td>
            </tr>
            <tr>
                <td>PCBS không xác định</td> <td>{df["t_pcbskxd"][0]}</td>
                <td></td> <td></td>
            </tr>
            <tr>
                <td>Tiền ăn giữa ca</td> <td>{df["t_tagc"][0]}</td>
                <td></td> <td></td>
            </tr>
            <tr>
                <td>Chống nóng</td> <td>{df["t_cn"][0]}</td>
                <td></td> <td></td>
            </tr>
            <tr>
                <td style="background-color: #edb528;"></td>
                <td style="background-color: #edb528;"></td>
                <td style="background-color: #edb528;"><b>Còn lại thực nhận</b></td>
                <td style="background-color: #edb528;"><b>{df["residual"][0]}</b></td>
            </tr>

            
        </thead>

        
        <tfoot>
            <tr>
                <!-- <th colspan="2">Thành tiền đơn hàng</th>
                <th colspan="2">{df["total"][0]}</th> -->
            </tr>
            <tr>
                <th colspan="2" style="text-align: center;">Tổng mức bảo hiểm Công ty đóng cho NLĐ</th>
                <th colspan="2">{df["insurance"][0]}</th>
            </tr>
            <tr>
                <td colspan="2">Bảo hiểm xã hội (17,5%)</td>
                <td colspan="2">{df["i_bhxh"][0]}</td>
            </tr>
            <tr>
                <td colspan="2">Bảo hiểm y tế (3%)</td>
                <td colspan="2">{df["i_bhyt"][0]}</td>
            </tr>
            <tr>
                <td colspan="2">Bảo hiểm thất nghiệp (1%)</td>
                <td colspan="2">{df["i_bhtn"][0]}</td>
            </tr>
        </tfoot>
        
    </table>

    <!-- Information contact -->
    <div class="end" >
        <p style="line-height: 1.7; font-size: 120%; margin-left: 80px;"> 
            Chân thành cảm ơn sự đóng góp của {df["gender"][0]} {df["name_u"][0]} ! 
            <br>Mong Anh luôn giữ gìn sức khỏe để gặt hái thêm nhiều thành công tại Công ty. 
            <br>Mọi ý kiến phản hồi vui lòng liên hệ trực tiếp trong hộp thư này, hoặc theo số điện thoại dưới đây. 
            <br><b>Trân trọng.</b>
            <br>Phòng Tổ chức – Tiền lương | Công ty Cổ phần Cảng Đà Nẵng.
            <br>SĐT: 0236 3 822 508 hoặc 0977 545 747 (gặp Trần Thị Quý Thanh).
        </p> 
    </div>
    """
    css = """
    u {
        color:#2d2e2e;
        text-decoration: none;
    }
    #values{
        text-transform: uppercase;
    }
    .header {
        line-height: 0.9;
        font-size: 90%;
        
    }
    .col-wrap {
    display: table;
    width: 100%;
    }

    .col {
    display: table-cell;
    padding: 1rem
    }
    /* ----------------------- */
    /* Cấu trúc bảng */
    .content{
        width: 100%;
        border:2px solid black;border-collapse:collapse;
        margin-left:auto;
        margin-right:auto;
        font-size: 110%;

    }

    td, th {
        border:1px solid black;border-collapse:collapse;
        height: 40px;
    }

    /* Cột không in đậm */
    td:nth-child(odd) {  
        background-color: #fff;  
        text-align: left;
        padding-left: 2.5%;
        width: 35%;
    } 
    td:nth-child(even) {  
        /* background-color: rgb(161, 56, 56); */
        text-align: right;  
        padding-right: 2.5%;
    } 
    /* Cột in đậm */
    th:nth-child(odd) {  
        background-color: #fff;  
        text-align: left;
        padding-left: 2.5%;
    } 
    th:nth-child(even) {  
        /* background-color: rgb(161, 56, 56); */
        text-align: right;  
        padding-right: 2.5%;
    }
    """
    name_img = "salary.png"
    with open("readme.txt", "w") as f:
        f.write("Create a new text file!")
    hti = Html2Image()
    print(hti.screenshot(html_str=html, css_str=css, save_as = name_img, size=(1350,2222)))
    from os import walk
    filenames = next(walk("./"), (None, None, []))[2]
    print(filenames)
    #-----------------UPLOAD IMAGE TO SERVER ZALO
    import requests
    import json
    url = "https://openapi.zalo.me/v2.0/oa/upload/image"
    files = [
          ("file",("file",open(name_img,"rb"),"multipart/form-data"))
        ]
    access_token = "TZTpOTD3Pd1xDd1bta5dT7i_U6BHLmSFALWCGVfxKWS-2Z51roPcItWF546KFtuYFXejSDKFQGqiVY1frMyrFNv78pUBPsX5P7KU8wv1MIbSR0n0y6vC2YX247pgO6Pk6sbtCyXdCqjXMLuvj5CQNKPaPWYF5IfC82Tv4v1O2dzXRM0PjbiWRr9sJpwkSGjiN4Dw1Orj1KnuNta1h4vlRtTT3Hs1Q7ngSHmO9veGH49IOoWhjKHxQtTd90cTS7T2U7aPLhLPKYvRK2r-dbvV4ZH93b_EFK5E118o0yPdTKmZIm8n_Mb0S59T107_U19nBNLu5TrKBLWVI4HFdKOc9zzVP7u"
    headers = { "access_token": access_token }
    response = requests.request("POST", url, headers = headers, files=files)
    
    #---------------SEND IMAGE TO USER
    if response.ok:
        end_point = "https://openapi.zalo.me/v2.0/oa/message"
        user_id = df["id_zalo"][i]
        text = f"""BẢNG LƯƠNG CHI TIẾT THÁNG {month} NĂM {year} - {df["gender"][0]} {df["name_u"][0]} (Mã: {df["id_nv"][0]})"""
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
                        # "url": "https://interactive-examples.mdn.mozilla.net/media/cc0-images/grapefruit-slice-332-332.jpg"
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
        status = "create image failed"   
    time = datetime.now()
    df_check.append({"id_send":i, "id_zalo": df["id_zalo"][i], "id_salary": df["id_l"][0], "time_send": time, "status": status})
OutputDataSet = pd.DataFrame.from_dict(df_check, orient="columns")
		'
			, @input_data_1 = @input_data;

		--> Lưu kết quả log lại cho người dùng
		SELECT * FROM @RESULT_POST
		DECLARE @id_send int = (select ISNULL(max(id_send),0) from zalo_salary_send)

		INSERT INTO dbo.zalo_salary_send 
			SELECT (id_send + @id_send), id_zalo, id_salary, time_send, status FROM @RESULT_POST

	END

END

--select * from zalo_salary_send
--select * from zalo_user
--select * from zalo_luong
--update zalo_user
--set department = N'Quan hệ quốc tế'
--where id_user = 4





	
