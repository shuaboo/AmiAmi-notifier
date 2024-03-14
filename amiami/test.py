def add(productInfo):
    # for future reference
    # there seems to be 3 different stock flags
    # stock, stock_flg and instock_flg
    # stock seems to be only for the item page itself, not the results page
    # stock_flg seems to be 1 everywhere no matter what
    # instock_flg seems to be 1 when you can click to order the item HOWEVER
    # instock_flg will be 0 on the item page itself, but not on the results
    # therefore, we use instock since we're using results page
    inStock = productInfo['instock_flg'] == 1
    # is_closed seems to reflect whether or not the item is actually closed
    isClosed = productInfo['order_closed_flg'] == 1
    # the next 2 seemed simple enough
    isPreorder = productInfo['preorderitem'] == 1
    isBackorder = productInfo['list_backorder_available'] == 1
    # this was found by looking at the filter they provide and seeing the
    # s_st_condition_flag query they pass. Not sure entirely yet, but seems
    # to be ok so far?
    isPreOwned = productInfo['condition_flg'] == 1
    # finally, we have these
    flags = {
        "instock": inStock,
        "isclosed": isClosed,
        "ispreorder": isPreorder,
        "isbackorder": isBackorder,
        "ispreowned": isPreOwned,
    }
    availability = "Unknown status?"
    if isClosed:
        if isPreorder:
            availability = "Pre-order Closed"
        elif isBackorder:
            availability = "Back-order Closed"
        else:
            availability = "Order Closed"
    elif isBackorder:
        availability = "Back-order"
    else:
        if isPreorder and inStock:
            availability = "Pre-order"
        if isPreorder and not inStock:
            availability = "Pre-order Closed"
        elif isPreOwned and inStock:
            availability = "Pre-owned"
        elif inStock:
            availability = "Available"

    print(flags)
    return availability


item =     {
    "gcode": "GOODS-04230787",
      "gname": "[Bonus] Touhou Plush Series 57 [Toyosatomimi no Miko] Fumofumo Miko.",
      "thumb_url": "/images/product/main/222/GOODS-04230787.jpg",
      "thumb_alt": "GOODS-04230787.jpg",
      "thumb_title": "[Bonus] Touhou Plush Series 57 [Toyosatomimi no Miko] Fumofumo Miko.",
      "min_price": 4400,
      "max_price": 4400,
      "c_price_taxed": 4400,
      "maker_name": "Gift",
      "saleitem": 0,
      "condition_flg": 0,
      "list_preorder_available": 0,
      "list_backorder_available": 0,
      "list_store_bonus": 0,
      "list_amiami_limited": 0,
      "instock_flg": 1,
      "order_closed_flg": 0,
      "element_id": "null",
      "salestatus": "",
      "salestatus_detail": "",
      "releasedate": "2022/06/30 0:00:00",
      "jancode": "4580731021339",
      "preorderitem": 0,
      "saletopitem": 0,
      "resale_flg": 0,
      "preowned_sale_flg": "null",
      "for_women_flg": 0,
      "genre_moe": 1,
      "cate6": "null",
      "cate7": "null",
      "buy_flg": 0,
      "buy_price": 0,
      "buy_remarks": "null",
      "stock_flg": 1,
      "image_on": 1,
      "image_category": "222/",
      "image_name": "GOODS-04230787",
      "metaalt": "null"
    }
  

print(add(item))