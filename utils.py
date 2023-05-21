def get_database_config_variables(url):
    """
    Parse the Heroku `DATABASE_URL` into a dictionary.
    """
    # Remove the `postgres://` from the beginning of the string
    url = url.split('://')[1]
    # Split the remaining string into a list on the `@` character, which
	# separates the database credentials from the host info
    credentials_and_host_info = url.split('@')
    # Get the database credentials (`DATABASE_USER` and `DATABASE_PASSWORD`)
	# from the first item in the `credentials_and_host_info` list
    credentials = credentials_and_host_info[0].split(':')
    # Get the database `host_info` from the second item in the
	# `credentials_and_host_info` list, which is the `DATABASE_HOST`,
	# `DATABASE_PORT`, and `DATABASE_NAME`
    host_info = credentials_and_host_info[1].split(':')
    # Get the database host from the first item in the `host_info` list
    host = host_info[0]
    # Get the database port and name from the second item in the
	# `host_info` list
    port_and_name = host_info[1].split('/')
    # Get the database port from the first item in the `port_and_name` list
    port = port_and_name[0]
    # Get the database name from the second item in the `port_and_name` list
    name = port_and_name[1]
    # Return a dictionary with the database credentials and host info
    return {
        'DATABASE_USER': credentials[0],
        'DATABASE_PASSWORD': credentials[1],
        'DATABASE_HOST': host,
        'DATABASE_PORT': port,
        'DATABASE_NAME': name
    }