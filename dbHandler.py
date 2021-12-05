import dbConnection as db

def getContents(base_id, series, keyword, sort, order, size, page):
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
                LEFT JOIN series s
                        ON s.base_dir_id = c.base_dir_id
                        AND s.series_id = c.series_id
        WHERE """

    if base_id == 0:
        query += """
            base.base_dir_id >= %s
            """ % (base_id)
    else:
        query += """
            base.base_dir_id = %s
            """ % (base_id)
    if series is not None:
        query += """
            AND s.series_id = %s
            """ % (series)

    query += """
        AND c.full_contents_name LIKE %s
        ORDER BY %s %s
        LIMIT %s
        OFFSET %s
    """ % (keyword, sort, order, size, page)

    print(query)

    return db.selectQuery(query)

def getGenres(base_id):
    query = """
        SELECT 
            genre_id
            ,genre
        FROM 
            genre 
        WHERE 
            base_dir_id = %s
        
        ORDER BY count DESC
        """ % (base_id)
    print(query)
    return db.selectQuery(query)

def getSeries(base_id):
    query = """
        SELECT 
            series_id
            , series_name
        FROM 
            series 
        WHERE 
            base_dir_id = %s
        
        ORDER BY series_name ASC
        """ % (base_id)
    print(query)
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