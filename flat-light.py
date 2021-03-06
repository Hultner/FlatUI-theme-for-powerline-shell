class Color(DefaultColor):
    USERNAME_FG = 0
    USERNAME_BG = 15
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 15
    HOSTNAME_BG = 14

    HOME_SPECIAL_DISPLAY = False
    PATH_FG = 0
    PATH_BG = 15
    CWD_FG = 0
    SEPARATOR_FG = 14

    READONLY_BG = 1
    READONLY_FG = 7

    REPO_CLEAN_FG = 15 
    REPO_CLEAN_BG = 2
    REPO_DIRTY_FG = 15
    REPO_DIRTY_BG = 9

    JOBS_FG = 0
    JOBS_BG = 8

    CMD_PASSED_FG = 15
    CMD_PASSED_BG = 14
    CMD_FAILED_FG = 1
    CMD_FAILED_BG = 15

    SVN_CHANGES_FG = REPO_DIRTY_FG
    SVN_CHANGES_BG = REPO_DIRTY_BG

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 15
