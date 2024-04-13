class UserData:
    ACCEPTED_USERNAMES = ['standard_user', 'performance_glitch_user',
                          'visual_user']
    PASSWORD = 'secret_sauce'
    INVALID_USERNAME = 'user'
    INVALID_PASSWORD = 'password'
    ORDER_INVALID_DATA = (
        ('', 'Baker', '227659', 'Error: First Name is required'),
        ('Stive', '', '227659', 'Error: Last Name is required'),
        ('Stive', 'Baker', '', 'Error: Postal Code is required')
    )
    ORDER_VALID_DATA = ('Stive', 'Baker', '227659')
