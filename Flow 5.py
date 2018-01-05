[
    {
        "id": "37a26712.c9c408",
        "type": "tab",
        "label": "Flow 5"
    },
    {
        "id": "9f98b4e0.c034f8",
        "type": "http in",
        "z": "37a26712.c9c408",
        "name": "Set GPIO5",
        "url": "/setgpio5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 155,
        "y": 213,
        "wires": [
            [
                "c3a237a7.9ec7f8",
                "1290da84.c9e4a5"
            ]
        ]
    },
    {
        "id": "c3a237a7.9ec7f8",
        "type": "function",
        "z": "37a26712.c9c408",
        "name": "Set to 1",
        "func": "msg.payload= 1;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 340,
        "y": 320,
        "wires": [
            [
                "41c77d00.77dd04"
            ]
        ]
    },
    {
        "id": "41c77d00.77dd04",
        "type": "rpi-gpio out",
        "z": "37a26712.c9c408",
        "name": "",
        "pin": "7",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 550,
        "y": 420,
        "wires": []
    },
    {
        "id": "1290da84.c9e4a5",
        "type": "function",
        "z": "37a26712.c9c408",
        "name": "Return Status",
        "func": "msg.payload=\"GPIO5 set to HIGH\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 360,
        "y": 140,
        "wires": [
            [
                "83497641.06c888",
                "d041a788.f25118"
            ]
        ]
    },
    {
        "id": "83497641.06c888",
        "type": "http response",
        "z": "37a26712.c9c408",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 830,
        "y": 400,
        "wires": []
    },
    {
        "id": "d041a788.f25118",
        "type": "debug",
        "z": "37a26712.c9c408",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 850,
        "y": 460,
        "wires": []
    },
    {
        "id": "7688d1f0.7cf65",
        "type": "http in",
        "z": "37a26712.c9c408",
        "name": "Clear GPIO5",
        "url": "/clear5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 150,
        "y": 500,
        "wires": [
            [
                "4466ce9d.24534",
                "3e4b03aa.e5417c"
            ]
        ]
    },
    {
        "id": "4466ce9d.24534",
        "type": "function",
        "z": "37a26712.c9c408",
        "name": "Clear to 0",
        "func": "msg.payload=0;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 340,
        "y": 500,
        "wires": [
            [
                "41c77d00.77dd04"
            ]
        ]
    },
    {
        "id": "3e4b03aa.e5417c",
        "type": "function",
        "z": "37a26712.c9c408",
        "name": "Return Status",
        "func": "msg.payload=\"GPIO5 set to LOW\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 380,
        "y": 620,
        "wires": [
            [
                "83497641.06c888",
                "d041a788.f25118"
            ]
        ]
    }
]
