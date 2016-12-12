import xml.etree.ElementTree as ET

EMPTY_STRING = ""
NAME_STR = "ItemName"
CODE_STR = "ItemCode"
PRICE_STR = "ItemPrice"
OPEN_CHAR = "["
CLOSE_CHAR = "]"


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
    for item in store_items:
        item_code = item.find(CODE_STR).text
        item_attributes = dict()   # empty dict for each item
        for attribute in item:
            item_attributes[attribute.tag] = attribute.text
        store_db[item_code] = item_attributes
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
    str_to_check = None  # value if there wasn't open char before
    result_list = []
    for char in basket_txt:
        if char is OPEN_CHAR:
            str_to_check = EMPTY_STRING  # Value shows we had open char
        elif char is CLOSE_CHAR:
            if str_to_check is not None:
                # if we got to the end of this part and have content
                result_list.append(str_to_check)
            str_to_check = None  # reset value for the next round
        elif str_to_check is not None:
            # if we still didn't find close char but had open,
            # keep adding letters
            str_to_check = str_to_check + char
        else:
            str_to_check = None
    return result_list

    # user_basket = []  # a list to fill the basket
    # starting_bracket_index = basket_txt.find('[')
    # while starting_bracket_index is not -1:
    #     # -1 is the return value of find() if did not find the string
    #     ending_bracket_index = basket_txt.find(']', starting_bracket_index)
    #     if ending_bracket_index == -1:
    #         break
    #     else:
    #         item_code = basket_txt[
    #                     starting_bracket_index + 1:ending_bracket_index]
    #         # the code is between the brackets
    #         user_basket.append(item_code)
    #         # clip the basket txt and try to find another '['
    #         basket_txt = basket_txt[ending_bracket_index:]
    #         starting_bracket_index = basket_txt.find('[')
    #
    # return user_basket


def get_basket_prices(store_db, basket):
    """
    Arguments: a store - dictionary of dictionaries and a basket -
       a list of ItemCodes
    Go over all the items in the basket and create a new list
      that describes the prices of store items
    In case one of the items is not part of the store,
      its price will be None.

    """
    price_list = []     # the list of prices
    for item in basket:
        if item in store_db.keys():
            price_list.append(float(store_db[item][PRICE_STR]))
        else:
            price_list.append(None)
    return price_list


def sum_basket(price_list):
    """
    Receives a list of prices
    Returns a tuple - the sum of the list (when ignoring Nones)
      and the number of missing items (Number of Nones)

    """
    missing_items_counter = 0
    basket_sum = 0  # starting value printed if all are None
    for price in price_list:
        if price is None:
            missing_items_counter += 1
        else:
            basket_sum += price
    return basket_sum, missing_items_counter


def basket_item_name(stores_db_list, ItemCode):
    """
    stores_db_list is a list of stores (list of dictionaries of
      dictionaries)
    Find the first store in the list that contains the item and return its
    string representation (as in string_item())
    If the item is not avaiable in any of the stores return only [ItemCode]

    """
    for store in stores_db_list:
        if ItemCode in store.keys():
            return store[ItemCode][NAME_STR]
    return '['+ItemCode+']'



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
