from bs4 import BeautifulSoup

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    soup = BeautifulSoup(response.data, 'html.parser')
    
    # Check for the welcome card header
    assert "Welcome to the App" in soup.find('h4').text
    # Check for the button
    assert soup.find('button', class_='btn-primary') is not None

def test_expenses_page_loads(client):
    response = client.get('/expenses')
    assert response.status_code == 200
    soup = BeautifulSoup(response.data, 'html.parser')
    
    # Check for the card header
    assert "Add New Expense" in soup.find('h4').text

def test_expenses_form_fields(client):
    response = client.get('/expenses')
    soup = BeautifulSoup(response.data, 'html.parser')
    
    # Check for all required fields
    assert soup.find('input', id='expenseName') is not None
    assert soup.find('input', id='expenseCategory') is not None
    assert soup.find('select', id='expenseItem') is not None
    assert soup.find('input', id='expenseCost') is not None
    assert soup.find('input', id='expenseDate') is not None

def test_item_type_multiselect(client):
    response = client.get('/expenses')
    soup = BeautifulSoup(response.data, 'html.parser')
    
    select_element = soup.find('select', id='expenseItem')
    # Check if 'multiple' attribute is present
    assert select_element.has_attr('multiple')
    
    # Check for some options
    options = [option.text for option in select_element.find_all('option')]
    assert "Grocery" in options
    assert "Toys" in options
    assert "Others" in options
