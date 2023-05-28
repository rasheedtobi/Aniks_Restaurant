from rest_framework.throttling import UserRateThrottle

class TwentyCallsPerMinute(UserRateThrottle):
    scopes = 'twenty' 