# Table

## zalo_user
    - id_user (int) <- Tăng mã tự động
    - name
    - birth
    - id_zalo
    - position
    - gender
    - phone
    - email

## zalo_salary
    - id_salary (int) <- Tăng mã tự động
    - id_user 
    - advance (advance payment)
    - remaining (Còn lại)
    - total
    - month
    - year
    - edit_date
    - status (chốt lương hay chưa)

## zalo_details_salary
    - id_salary
    - date
    - product
    - number
    - price
    - charge


## zalo_salary_send
    - id_send (int) <- Tăng mã tự động
    - id_zalo
    - time_send
    - status


# Procedure
    - Create (zalo_user)
    - Create (Tạo tự động)

