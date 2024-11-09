PRODUCTION = False

DB = {
    'influx_prod': {
        'url': 'http://127.0.0.1:9098',
        'token': 'xLh2BnswKUraKXJqWnOeHgrMIUdb61H2DqVIInVbWzivuB0nfBmIGb2leS3yZsLZOMFqAIKG5WFa8qDDfCtMgA==',
        'org': 'BlackIQ',
        'bucket': 'amir-monitoring',
    },
    'influx_local': {
        'url': 'http://127.0.0.1:8086',
        'token': 'aL7fOUnjYOMN1-aoyj3DMsMxJ44edgnN2Ts2Fv-uS5ZI2_CpsXo-17G57B5YMZLJ0wVuPoKIJ9d_HMHZOF9qPw==',
        'org': 'BlackIQ',
        'bucket': 'amir-monitoring',
    }
}