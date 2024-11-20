import firebase_admin
from firebase_admin import credentials, db

# Configuração do Firebase
firebase_config = {
  "type": "service_account",
  "project_id": "poc-project-cdac7",
  "private_key_id": "1ebaf8b1a0713d5ba45b6f34e4198760abd01130",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQClOXx4fLB0AEkJ\nCHuEKXcZkYhykIpuVg/OyTrBn53BowO+GakYUKLB0spbmPjKAKWXbeov4IU4wyjv\nJvQLc1l8lrf4TvDss5r8T3BFYYyd9X8mfdVQ6tJ2cReeLBJ3RMB/zdzNvgDJEeaX\nrm1fjHDH6m9+OmpJ7EMSyg535C0Fp956ddPty9b0KFJcWtHukQ1ShdU6rDjRNkiK\noIRaXenvn7bgfq5xYuvOFKFIGJxLXW6+od8P7UYajYgiYyjNgoB+9cIZNuzF8Z0x\nhv7mcxjWvppGAumKVauoyjohR8LhESvPU1D/BlCwUj9MFwzgaCqX+lTzxkuuBU7z\nW2qmXvVTAgMBAAECggEAGUvt5Lyif4AzrnBgCOIYXA/OJkw/BZmjnfNtTYvUqXr9\n7bMcEp717FsLpG6NWNA0ijTH8ECd5QzsTYFXSBGHF+4ziI79kCAHkK3Q8K54yw51\nQz1s1ZC+XGgAR7VTtnMOTgME1XNLx304Iu0PzdtAwTsBiwACmgLUWiIZiP2kbwL/\nrNEcMl/ghxqHD9mTjL48vRHZqgjUaTNCzIqcBaJippM2fHaUB962Z79j03OICk5V\n6X46DbdYOmvR+WFpq+k0ooTXTdvtqJ+uftN/0uF+xvDCxJgkgOQLoi95xzM5upKF\nWXMRfrIebmo1N7DEDuYLmwMtI9fxQ/EWPWlsm9HvIQKBgQDSaZJPYiFMclSs+zhc\nZNpVLoskeCvFq7/KBy6TQFSJD9l0FlGWe93vPnuNiZuGTNXD3oBACqBNn7ryGA6d\n3NGfb+AKpvbFcL6q+tbszZ+PDKeHa2p/5AS6zOb4E+NGcfAUuiRn/1anW2W+a5GE\nshdkrqBjPZ0SO3hVZGr3Cu2WGwKBgQDJBZeDb6aWx42VF6Pgr3qSgCtMzUF4wix0\nak3aCBCd7ag68J97gBapBM+ipdv1CQgljDBuMJYk4Pn37fmjPv6HDiDyakJPHpEC\nrqa3XLV+Cs20eKb6b8E8oJ4eNucKCa6jw3qpEY4oyEdJ+aCICVGTn5kcch11w4VQ\n9DxGxjBxKQKBgQCPoQD+rz2LsX+blOEkMLPY8ayJeH5osJR6k+x3F7Kc3PTTCWko\nD+WvKjespgJD6q8AxSFGlfpXAnHaUBGqMNHmw7drjg1lOVDt5cxQWQxR2ZGCHxDT\nvBJ+cOA491ps+9mmTGoNk37TPtB063ip2+ecEpfpJmXRzEaYA7QAbrU/gQKBgCsS\n+qtcUkr+yZTH8wKjN1WLBzw2wy+4E8SCPtpYXg8pLKIsi0/wW2quMDu+5In1/Hvn\nNT13RcTzPDznDlXvmqSf32lyYXEIsLPtbqXdxLoUYI2qSMVjCvoNxLPeudUJzBUl\nPvRZYafVeokcZ0yfCo7iZPGWdj+UvM1i+EOGFj05AoGAGF0Z6L77na+txdKXFu6f\npksLwr6om53qH9TEN+yLHI+Kv/za7ZV33Dx31lGjh6r55KoLRQuNDVlRTDizSTSX\nG/0610dn4oxyB2NTp49x9gSY4ZaXrPwE9Ed8wdmLEc+HBtfBcGHRZZyafUkjSdPd\nRoYRZI8RHf2DXIJYfMmUb+Q=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-694bu@poc-project-cdac7.iam.gserviceaccount.com",
  "client_id": "116446943411447461114",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-694bu%40poc-project-cdac7.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# Inicializar o app Firebase com credenciais e URL do Realtime Database
cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://poc-project-cdac7-default-rtdb.firebaseio.com/'  # URL do Realtime Database
})

