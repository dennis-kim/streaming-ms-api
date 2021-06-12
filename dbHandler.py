import dbConnection as db

def getContents(base_id, keyword, sort, order, size, page):
    query = """
        SELECT 
            contents_name
        FROM 
            contents c 
                INNER JOIN base_dir base 
                        ON base.base_dir_id = c.base_dir_id 
                        AND base.env = 'prd' 
        WHERE 
            base.base_dir_id = %s
            AND c.contents_name LIKE %s
        ORDER BY %s %s
        LIMIT %s
        OFFSET %s
    """ % (base_id, keyword, sort, order, size, page)

    return db.selectQuery(query)


def getComments(size, page):
    query = """
        SELECT 
	        message, 
	        create_date 
        FROM 
	        comment
        ORDER BY create_date DESC
        LIMIT %s
        OFFSET %s
    """ % (size, page)
    print(query)

    return db.selectQuery(query)

def postComments(comment):
    query = """
        INSERT 
        INTO 
            comment (message)
        VALUES (%s)
    """ % (comment)
    print(query)

    return db.selectQuery(query)