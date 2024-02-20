import streamlit as st

st.set_page_config(page_title='MK Print', page_icon=':art:', layout='wide')

def login():
    st.title("Login Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        valid_users = {"ahmed": "26468463", "tarek": "tarek", "youssef": "youssef", "mohamed": "mohamed"}

        if username in valid_users and password == valid_users[username]:
            st.success("Login Successful!")
            st.balloons()
            st.session_state.logged_in = True
        else:
            st.error("Invalid Username or Password")

def home():
    st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; height: 20vh; color: #3498db; font-family: 'Arial', sans-serif;">
            <h1 style="text-align: center;">MK Print</h1>
        </div>
                """, unsafe_allow_html=True)
    col1 , col2 = st.columns(2)
    with col1:
        st.header("Calculator  :bulb:")
        
        size_width = st.number_input('Enter the width (in cm): :straight_ruler:', key='width')
        size_height = st.number_input('Enter the height (in cm): :straight_ruler:', key='height')
        pieces = st.number_input('Enter the pieces : ', key='pieces')
    # ------------------------------------------------------------------------------------------------------
       # ---------------------Logic Meter--------------------------
        
        width_result = int((102 / (size_width + 0.3)))
        height_result = int((100 / (size_height + 0.3)))
        result_meter = width_result * height_result
    
    # ------------------Print Way Price---------------------
        
        Print_way_Price = 235
    
        width_result_Print_way = int((102 / (size_width + 0.3)))
        height_result_Print_way = int((85 / (size_height + 0.3)))
        result_meter_Print_way = width_result_Print_way * height_result_Print_way
        
        industrial_cost_Print_way = int((pieces / result_meter_Print_way) * Print_way_Price)
        price_of_work_Print_way= int(pieces / result_meter * 300)
        profit_Print_way = price_of_work_Print_way - industrial_cost_Print_way
        
    # ------------------Print Uptown Price---------------------
        
        Print_uptown_Price = 200
        
        width_result_Print_uptown = int((96 / (size_width + 0.3)))
        height_result_Print_uptown = int((90 / (size_height + 0.3)))
        result_meter_Print_uptown = width_result_Print_uptown * height_result_Print_uptown
    
        industrial_cost_Print_uptown = int((pieces / result_meter_Print_uptown) * Print_uptown_Price)
        price_of_work_Print_uptown = int(pieces / result_meter * 300)
        profit_Print_uptown = price_of_work_Print_uptown - industrial_cost_Print_uptown
    # ------------------------------------------------------------------------------------------------------------------
        
        
        
        if st.button("Calculate"):
    # ------------------Print Way Price---------------------
            st.write('------------------Print Way------------------')
            st.write(f'For a shape of size {size_width} cm')
            st.write(f'There are approximately {width_result_Print_way} pieces in width lines in one meter.')
    
            st.write(f'For a shape of size {size_height} cm')
            st.write(f'There are approximately {height_result_Print_way} pieces in width lines in one meter.')
    
            st.write(f'For a shape of size {size_width} cm x {size_height} cm')
            st.write(f'Meter has approximately {result_meter_Print_way} shape.')
    
            st.write(f'Industrial cost {industrial_cost_Print_way}EGP.') 
    
            st.write(f'Price of work {price_of_work_Print_way}EGP.')
    
            st.write(f'Profit {profit_Print_way}EGP.')  
    
    # ------------------Print Uptown Price---------------------
    
            st.write('------------------UPtown Print------------------')
            st.write(f'For a shape of size {size_width} cm')
            st.write(f'There are approximately {width_result_Print_uptown} pieces in width lines in one meter.')
        
            st.write(f'For a shape of size {size_height} cm')
            st.write(f'There are approximately {height_result_Print_uptown} pieces in width lines in one meter.')
    
            st.write(f'For a shape of size {size_width} cm x {size_height} cm')
            st.write(f'Meter has approximately {result_meter_Print_uptown} shape.')
     
            st.write(f'Industrial cost {industrial_cost_Print_uptown}EGP.') 
    
            st.write(f'Price of work {price_of_work_Print_uptown}EGP.')
    
            st.write(f'Profit {profit_Print_uptown}EGP.')  
            
    with col2:
        st.header("Calculator another printing company  :bulb: ")

        meter_width_another_printing_company = st.number_input('Enter the meter width (in cm): :straight_ruler:', key='meter_width_another_printing_company')
        meter_height_another_printing_company = st.number_input('Enter the meter height (in cm): :straight_ruler:', key='meter_height_another_printing_company')
        size_width_another_printing_company = st.number_input('Enter the width (in cm): :straight_ruler:', key='size_width_another_printing_company')
        size_height_another_printing_company = st.number_input('Enter the height (in cm): :straight_ruler:', key='size_height_another_printing_company')
        pieces_another_printing_company = int(st.number_input('Enter the pieces : ', key='pieces_another_printing_company'))
        
 # ------------------another printing company Price---------------------
        
        another_printing_company_price = int(st.number_input('Enter the price of meter : ', key='price'))
    # ------------------------------------------------------------------------------------------------------
        width_result_another_printing_company_1 = int((102 / (size_width_another_printing_company + 0.3)))
        height_result_another_printing_company_1 = int((100 / (size_height_another_printing_company + 0.3)))
        result_meter_another_printing_company_1 = width_result_another_printing_company_1 * height_result_another_printing_company_1
    # ------------------------------------------------------------------------------------------------------
        width_result_another_printing_company = int((meter_width_another_printing_company / (size_width_another_printing_company + 0.3)))
        height_result_another_printing_company = int((meter_height_another_printing_company / (size_height_another_printing_company + 0.3)))
        result_meter_another_printing_company = width_result_another_printing_company * height_result_another_printing_company
    # ------------------------------------------------------------------------------------------------------        
        industrial_cost_another_printing_company = int((pieces_another_printing_company / result_meter_another_printing_company) * another_printing_company_price)
        price_of_work_another_printing_company= int(pieces_another_printing_company / result_meter_another_printing_company_1 * 300)
        profit_another_printing_company = price_of_work_another_printing_company - industrial_cost_another_printing_company

# ------------------another printing company Price---------------------
        if st.button("Calculate_another_printing_company"):
            
            st.write('------------------another printing company------------------')
            st.write(f'For a shape of size {size_width_another_printing_company} cm')
            st.write(f'There are approximately {width_result_another_printing_company} pieces in width lines in one meter.')
        
            st.write(f'For a shape of size {size_height_another_printing_company} cm')
            st.write(f'There are approximately {height_result_another_printing_company} pieces in width lines in one meter.')
    
            st.write(f'For a shape of size {size_width_another_printing_company} cm x {size_height_another_printing_company} cm')
            st.write(f'Meter has approximately {result_meter_another_printing_company} shape.')
     
            st.write(f'Industrial cost {industrial_cost_another_printing_company}EGP.') 
    
            st.write(f'Price of work {price_of_work_another_printing_company}EGP.')
    
            st.write(f'Profit {profit_another_printing_company}EGP.')




def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        home()
    else:
        login()

if __name__ == "__main__":
    main()
