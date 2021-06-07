import dbConnection as db

def getContents(base_id, sort, order):
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
            ORDER BY %s %s
    """ % (base_id, sort, order)

    return db.selectQuery(query)