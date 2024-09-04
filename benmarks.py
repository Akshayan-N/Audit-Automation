files_benmarks =  [
    {
        "path" : "/etc/passwd",
        "permissions" : [["read", "write"], ["read"], ["read"]],
        "group" : ["root"],
        "cmd_fix": "chmod 644 ",      
    },
    {
        "path" : "/etc/group",
        "permissions" : [["read", "write"], ["read"], ["read"]],
        "group" : ["root"],
        "cmd_fix": "chmod 644 ",
    },
    {
        "path" : "/etc/shadow",
        "permissions" : [["read", "write"], ["read"], []],
        "group": ["root"],
        "cmd_fix": "chmod o-rwx,g-wx "  
    },
    {
        "path" : "/etc/gshadow",
        "permissions" : [["read", "write"], ["read"], []],
        "group": ["root"],
        "cmd_fix": "chmod o-rwx,g-wx "  
    },
    {
        "path" : "/etc/shadow-",
        "permissions" : [["read", "write"], ["read"], []],
        "group": ["root", "shadow"],
        "cmd_fix": "chmod o-rwx,g-wx "  
    },
    {
        "path" : "/etc/gshadow-",
        "permissions" : [["read", "write"], ["read"], []],
        "group": ["root", "shadow"],
        "cmd_fix": "chmod o-rwx,g-wx "  
    },
    {
        "path" : "/etc/passwd-",
        "permissions" : [["read", "write"], [], []],
        "group" : ["root"],
        "cmd_fix": "chmod u-x,go-rwx ",
    },
    {
        "path" : "/etc/group-",
        "permissions" : [["read", "write"], ["read"], ["read"]],
        "group" : ["root"],
        "cmd_fix": "chmod u-x,go-rwx ",
    },
]