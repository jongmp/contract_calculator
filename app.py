# import statements
import streamlit as st  

# Defining Federal Tax
fed_tax = 0.215

state_options = {"ALABAMA":"0.04",
                    "ALASKA":"0",
                    "ARIZONA"	:"0.04",
                    "ARKANSAS"	:"0.04",
                    "CALIFORNIA"	:"0.07",
                    "COLORADO"	:"0.05",
                    "CONNECTICUT"	:"0.05",
                    "DELAWARE"	:"0.04",
                    "FLORIDA"	:"0",
                    "GEORGIA"	:"0.04",
                    "HAWAII"	:"0.06",
                    "IDAHO"	:"0.04",
                    "ILLINOIS"	:"0.05",
                    "INDIANA"	:"0.03",
                    "IOWA"	:"0.04",
                    "KANSAS"	:"0.05",
                    "KENTUCKY"	:"0.05",
                    "LOUISIANA"	:"0.03",
                    "MAINE"	:"0.06",
                    "MARYLAND"	:"0.04",
                    "MASSACHUSETTS"	:"0.05",
                    "MICHIGAN"	:"0.04",
                    "MINNESOTA"	:"0.07",
                    "MISSISSIPPI"	:"0.03",
                    "MISSOURI"	:"0.03",
                    "MONTANA"	:"0.03",
                    "NEBRASKA"	:"0.04",
                    "NEVADA"	:"0",
                    "NEW HAMPSHIRE":"0",
                    "NEW JERSEY"	:"0.06",
                    "NEW MEXICO"	:"0.04",
                    "NEW YORK"	:"0.09",
                    "NORTH CAROLINA"	:"0.05",
                    "NORTH DAKOTA"	:"0.02",
                    "OHIO"	:"0.02",
                    "OKLAHOMA"	:"0.03",
                    "OREGON"	:"0.07",
                    "PENNSYLVANIA"	:"0.03",
                    "RHODE ISLAND"	:"0.04",
                    "SOUTH CAROLINA"	:"0.04",
                    "SOUTH DAKOTA":"0",
                    "TENNESSEE":"0",
                    "TEXAS":"0",
                    "UTAH"	:"0.05",
                    "VERMONT"	:"0.05",
                    "VIRGINIA"	:"0.03",
                    "WASHINGTON":"0",
                    "WEST VIRGINIA"	:"0.05",
                    "WISCONSIN"	:"0.06",
                    "WYOMING":"0",
                    "DIST. OF COLUMBIA"	:"0.06"}     

# Page Configuarion
st.set_page_config(layout="wide")

# Side Bar 
st.sidebar.title("Base Contract Information")
st.sidebar.info("Please fill in your base salary, base rent, and home state below")

# Inputs for Base Salary 
base_salary = st.sidebar.number_input("Please enter your base monthly salary ($)", min_value=0, max_value=20000, value=4000, step=100)
base_stipend = st.sidebar.number_input("Please enter your base monthly stipend ($)", min_value=0, max_value=20000, value=1000, step=100)
base_rent = st.sidebar.number_input("Please enter your base monthly rent ($)", min_value=0, max_value=20000, value=1500, step=100)
home_state = st.sidebar.selectbox("Please pick your home state", key = "base", options = state_options.keys())

# Calculating Current Post Tax Monthly Salary 
base_tax_rate = float(state_options[home_state])
base_total_tax_rate = base_tax_rate + fed_tax

# Post Tax Monthly Salary 
st.sidebar.write("\n")

post_base_salary = base_salary * (1 - base_total_tax_rate) + base_stipend
st.sidebar.write("""Post Tax Base Monthly Salary \n
                 $""" + str(int(post_base_salary)))

# Post Tax and Rent Take Home
st.sidebar.write("""Post Tax and Rent Take Home is \n
                 $""" + str(int(post_base_salary - base_rent)))

# Main Page
st.title("Travel Contract Comparison")
st.info("Please enter your monthly salary, stipend, rent, and state to calculate your take home pay for each contract and base contract")

# Setting Up Columns
columns = st.columns(3, gap="large")

with columns[0]:
# Option 1 
    st.text_input(label = "Contract 1", placeholder = "Please enter a name for your contract")
    container_one = st.container()
    # Inputs for Base Salary 
    opt_one_salary = container_one.number_input("**Please enter your monthly salary ($)**", min_value=0, max_value=20000, value=6000, step=100)
    opt_one_stipend = container_one.number_input("Please enter your monthly stipend ($)", min_value=0, max_value=20000, value=1000, step=100)
    opt_one_rent = container_one.number_input("Please enter your monthly rent ($)", min_value=0, max_value=20000, value=2000, step=100)
    opt_one_state = container_one.selectbox("Please pick your home state", key = "opt_one", options = state_options.keys())

    # Calculating Current Post Tax Monthly Salary 
    base_tax_rate = float(state_options[opt_one_state])
    base_total_tax_rate = base_tax_rate + fed_tax

    opt_one_post_tax_sal = opt_one_salary * (1 - base_total_tax_rate) + opt_one_stipend
    st.write("""Post Tax Base Monthly Salary \n
                    $""" + str(int(opt_one_post_tax_sal)))

    # Post Tax and Rent Take Home
    st.write("""Post Tax and Rent Take Home (Factoring in Home Rent) is \n
                    $""" + str(int(opt_one_post_tax_sal - opt_one_rent - base_rent)))
    
    # In one month, you would make this much more 
    st.write("""In 1 month, you would make this much more/less compared to your base\n
                    $""" + str(int(opt_one_post_tax_sal - post_base_salary - opt_one_rent - base_rent)))

    # In 3 months, you would make this much more
    st.write("""In 3 months, you would make this much more/less compared to your base\n
                    $""" + str(int(3 * (opt_one_post_tax_sal - post_base_salary - opt_one_rent - base_rent))))

with columns[1]:
# Option 2
    st.text_input(label = "Contract 2", placeholder = "Please enter a name for your contract")
    # Inputs for Base Salary 
    opt_two_salary = st.number_input("Please enter your monthly salary ($)", key = "opt_two_sal", min_value=0, max_value=20000, value=9000, step=100)
    opt_two_stipend = st.number_input("Please enter your monthly stipend ($)", min_value=0, max_value=20000, value=1500, step=100, key = 'opt_two_stip')
    opt_two_rent = st.number_input("Please enter your monthly rent ($)", key = "opt_two_rent", min_value=0, max_value=20000, value=2000, step=100)
    opt_two_state = st.selectbox("Please pick your home state", key = "opt_two_state", options = state_options.keys())

    # Calculating Current Post Tax Monthly Salary 
    base_tax_rate = float(state_options[opt_two_state])
    base_total_tax_rate = base_tax_rate + fed_tax

    opt_two_post_tax_sal = opt_two_salary * (1 - base_total_tax_rate) + opt_two_stipend
    st.write("""Post Tax Base Monthly Salary \n
                    $""" + str(int(opt_two_post_tax_sal)))

    # Post Tax and Rent Take Home
    st.write("""Post Tax and Rent Take Home (Factoring in Home Rent) is \n
                    $""" + str(int(opt_two_post_tax_sal - opt_two_rent - base_rent)))
    
    # In one month, you would make this much more 
    st.write("""In 1 month, you would make this much more/less compared to your base\n
                    $""" + str(int(opt_two_post_tax_sal - post_base_salary - opt_one_rent - base_rent)))

    # In 3 months, you would make this much more
    st.write("""In 3 months, you would make this much more/less compared to your base\n
                    $""" + str(int(3 * (opt_two_post_tax_sal - post_base_salary - opt_one_rent - base_rent))))
    
with columns[2]:
# Option 3
    st.text_input(label = "Contract 3", placeholder = "Please enter a name for your contract")
    # Inputs for Base Salary 
    opt_three_salary = st.number_input("Please enter your monthly salary ($)", key = "opt_three_sal", min_value=0, max_value=20000, value=8000, step=100)
    opt_three_stipend = st.number_input("Please enter your monthly stipend ($)", min_value=0, max_value=20000, value=2000, step=100, key = 'opt_three_stip')
    opt_three_rent = st.number_input("Please enter your monthly rent ($)", key = "opt_three_rent", min_value=0, max_value=20000, value=2000, step=100)
    opt_three_state = st.selectbox("Please pick your home state", key = "opt_three_state", options = state_options.keys())

    # Calculating Current Post Tax Monthly Salary 
    base_tax_rate = float(state_options[opt_three_state])
    base_total_tax_rate = base_tax_rate + fed_tax

    opt_three_post_tax_sal = opt_three_salary * (1 - base_total_tax_rate) + opt_three_stipend
    st.write("""Post Tax Base Monthly Salary \n
                    $""" + str(int(opt_three_post_tax_sal)))

    # Post Tax and Rent Take Home
    st.write("""Post Tax and Rent Take Home (Factoring in Home Rent) is \n
                    $""" + str(int(opt_three_post_tax_sal - opt_three_rent - base_rent)))
    
    # In one month, you would make this much more 
    st.write("""In 1 month, you would make this much more/less compared to your base\n
                    $""" + str(int(opt_three_post_tax_sal - post_base_salary - opt_one_rent - base_rent)))

    # In 3 months, you would make this much more
    st.write("""In 3 months, you would make this much more/less compared to your base\n
                    $""" + str(int(3 * (opt_three_post_tax_sal - post_base_salary - opt_one_rent - base_rent))))
