benchmarks = [
    {
        "path" : "/etc/shells",
        "permissions" : [["read", "write"], ["read"], ["read"]],
        "group" : ["root"],
        "cmd_fix": "chmod u-x,go-wx ",
    },
    {
        "path" : "/etc/security/opasswd",
        "permissions" : [["read", "write"], [], []],
        "group" : ["root"],
        "cmd_fix": "chmod u-x,go-wx ",
    },
    {
        "path" : "/etc/security/opasswd.old",
        "permissions" : [["read", "write"], [], []],
        "group" : ["root"],
        "cmd_fix": "chmod u-x,go-wx ",
    },
]