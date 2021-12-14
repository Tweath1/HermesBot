
import ssl
import pymongo

client = pymongo.MongoClient("mongodb+srv://sysAdmin:9gR7C1aDKclng4jA@cluster0.7s0ic.mongodb.net/Cluster0?retryWrites=true&w=majority?", tls=True, tlsAllowInvalidCertificates=True)