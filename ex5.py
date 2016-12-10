import xml.etree.ElementTree as ET

EMPTY_STRING = ""
NAME_STR = "ItemName"
CODE_STR = "ItemCode"
PRICE_STR = "ItemPrice"


def get_attribute(store_db, ItemCode, tag):
    """
    Returns the attribute (tag)
    of an Item with code: Itemcode in the given store
    """
    attribute_result = store_db[ItemCode][tag]
    return attribute_result


def string_item(item):
    """
    Textual representation of an item in a store.
    Returns a string in the format of '[ItemCode] (ItemName)'
    """
    result_string = "[" + item["ItemCode"] + "]\t" + "{" + item["ItemName"]+"}"
    return result_string


def string_store_items(store_db):
    """
    Textual representation of a store.
    Returns a string in the format of:
    string representation of item1
    string representation of item2
    """
    store_string = EMPTY_STRING
    for item in store_db:
        store_string = store_string + string_item(store_db[item]) + "\n"
    return store_string


def read_prices_file(filename):
    """
    Read a file of item prices into a dictionary.  The file is assumed to
    be in the standard XML format of "misrad haclcala".
    Returns a tuple: store_id and a store_db,
    where the first variable is the store name
    and the second is a dictionary describing the store.
    The keys in this db will be ItemCodes of the different items and the
    values smaller  dictionaries mapping attribute names to their values.
    Important attributes include 'ItemCode', 'ItemName', and 'ItemPrice'
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    store_id = root.find("StoreId").text
    store_items = root.find("Items").findall("Item")    # getting all the items
    store_db = dict()   # empty dict for the result
    # the next 3 vars will store the results
    item_code = EMPTY_STRING
    item_name = EMPTY_STRING
    item_price = EMPTY_STRING
    for item in store_items:
        item_code = item.find(CODE_STR).text
        item_name = item.find(NAME_STR).text
        item_price = item.find(PRICE_STR).text
        store_db[item_code] = {NAME_STR: item_name, PRICE_STR: item_price,
                               CODE_STR: item_code}
    return store_id, store_db


def filter_store(store_db, filter_txt):
    """
    Create a new dictionary that includes only the items
    that were filtered by user.
    I.e. items that text given by the user is part of their ItemName.
    Args:
    store_db: a dictionary of dictionaries as created in read_prices_file.
    filter_txt: the filter text as given by the user.
    """
    filtered_store = dict()
    for item in store_db:
        if filter_txt in store_db[item][NAME_STR]:
            filtered_store[item] = store_db[item]
    return filtered_store




def create_basket_from_txt(basket_txt):
    """
    Receives text representation of few items (and maybe some garbage
      at the edges)
    Returns a basket- list of ItemCodes that were included in basket_txt

    """
    pass


def get_basket_prices(store_db, basket):
    """
    Arguments: a store - dictionary of dictionaries and a basket -
       a list of ItemCodes
    Go over all the items in the basket and create a new list
      that describes the prices of store items
    In case one of the items is not part of the store,
      its price will be None.

    """
    pass


def sum_basket(price_list):
    """
    Receives a list of prices
    Returns a tuple - the sum of the list (when ignoring Nones)
      and the number of missing items (Number of Nones)

    """
    pass


def basket_item_name(stores_db_list, ItemCode):
    """
    stores_db_list is a list of stores (list of dictionaries of
      dictionaries)
    Find the first store in the list that contains the item and return its
    string representation (as in string_item())
    If the item is not avaiable in any of the stores return only [ItemCode]

    """
    pass


def save_basket(basket, filename):
    """
    Save the basket into a file
    The basket reresentation in the file will be in the following format:
    [ItemCode1]
    [ItemCode2]
    ...
    [ItemCodeN]
    """
    pass


def load_basket(filename):
    """
    Create basket (list of ItemCodes) from the given file.
    The file is assumed to be in the format of:
    [ItemCode1]
    [ItemCode2]
    ...
    [ItemCodeN]
    """
    pass


def best_basket(list_of_price_list):
    """
    Arg: list of lists, where each inner list is list of prices as created
    by get_basket_prices.
    Returns the cheapest store (index of the cheapest list) given that a
    missing item has a price of its maximal price in the other stores *1.25

    """
    pass
