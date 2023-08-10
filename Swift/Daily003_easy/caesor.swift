/**
 * CAESOR CYPHER
 *
 * challenge #3 (easy)
 * https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/
 *
 * sarthak7u@gmail.com
 */

func encrypt(_ string: String, _ key: Int) -> String {
    var encryptedString = ""
    for s in string {
        let code = s.asciiValue!
        if code >= 97 {
            let encrypted_code = (code - 97 + UInt8(key)) % 26 + 97
            encryptedString = encryptedString + String(UnicodeScalar(encrypted_code))
        } else if code == 32 {
            encryptedString = encryptedString + String(s)
        } else {
            let encrypted_code = (code - 65 + UInt8(key)) % 26 + 65
            encryptedString = encryptedString + String(UnicodeScalar(encrypted_code))
        }
    }

    return encryptedString
}

func decrypt(_ string: String, _ key: Int) -> String {
    var encryptedString = ""
    for s in string {
        let code = s.asciiValue!
        if code >= 97 {
            if Int(code) - 97 - key < 0 {
                let encrypted_code = code + 26 - UInt8(key)
                encryptedString = encryptedString + String(UnicodeScalar(encrypted_code))
            } else {
                let encrypted_code = code - UInt8(key)
                encryptedString = encryptedString + String(UnicodeScalar(encrypted_code))
            }
        } else if code == 32 {
            encryptedString = encryptedString + String(s)
        } else {
            if Int(code) - 65 - key < 0 {
                let encrypted_code = code + 26 - UInt8(key)
                encryptedString = encryptedString + String(UnicodeScalar(encrypted_code))
            } else {
                let encrypted_code = code - UInt8(key)
                encryptedString = encryptedString + String(UnicodeScalar(encrypted_code))
            }
        }
    }

    return encryptedString
}
