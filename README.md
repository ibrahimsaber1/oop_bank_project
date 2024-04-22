# Central Bank Library and Banking System

## Introduction:

The Central Bank Library and Banking System is a comprehensive Python program developed to facilitate digital library management and banking operations. It offers functionalities to manage library resources efficiently and enables users to perform banking transactions seamlessly.

## Library Management System:

### Task 1:

#### User Class:

- Attributes: `name`, `age`, `gender`, `balance`
- Method: `show_data` to display previous data

#### Bank Class:

- Inherits from User Class
- Methods: 
    - `deposit`: Add deposit amount to balance
    - `withdraw`: Withdraw amount from balance
    - `view_balance`: Display current balance

#### CIB Class (Child of Bank):

- Inherits from Bank Class
- Method: `loan_application` for loan application with constraints on loan amount and duration

#### QNB Class (Child of Bank):

- Inherits from Bank Class
- Method: `loan_application` for loan application with enhanced constraints on loan amount and duration

## Usage:

1. Clone the repository to your local machine.
2. Run the `https://github.com/ibrahimsaber1/library_system.git` file to manage library resources.
3. Run the `bank_application.py` file to perform banking transactions.

## Contributors:

- IBRAHIM SABER https://github.com/ibrahimsaber1 - Creator & Developer

## License:

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
