import dbConnection as db

def getContents(base_id, keyword, sort, order, size, page):
    query = """
        SELECT 
            IFNULL(c.contents_name, c.full_contents_name) as contents_name
            , c.sub_contents_name
            , c.genre
            , c.actors
            , base.dir_name as category_name
            , c.full_path as contents_path
            , c.thumbnail_url as thumbnail_url
            , c.modify_date
        FROM 
            contents c 
                INNER JOIN base_dir base 
                        ON base.base_dir_id = c.base_dir_id 
                        AND base.env = 'prd' 
        WHERE """

    if base_id == 0:
        query += """
            base.base_dir_id >= %s
            """ % (base_id)
    else:
        query += """
            base.base_dir_id = %s
            """ % (base_id)

    query += """
        AND c.full_contents_name LIKE %s
        ORDER BY %s %s
        LIMIT %s
        OFFSET %s
    """ % (keyword, sort, order, size, page)

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

    return db.selectQuery(query)

def postComments(comment):
    query = """
        INSERT 
        INTO 
            comment (message)
        VALUES (%s)
    """ % (comment)

    return db.selectQuery(query)