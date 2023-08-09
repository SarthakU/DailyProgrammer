/**
 * GAS LAW CALCULATOR
 *
 * challenge #2 (easy)
 * https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
 *
 * sarthak7u@gmail.com
 */

let R = 8.31446261815324

func calculate_pressure(_ V: Double, _ n: Double, _ T: Double) -> Double {
    return (n * R * T) / V
}

func calculate_volume(_ P: Double, _ n: Double, _ T: Double) -> Double {
    return (n * R * T) / P
}

func calculate_moles(_ P: Double, _ V: Double, _ T: Double) -> Double {
    return (P * V) / (R * T)
}

func calculate_temprature(_ P: Double, _ V: Double, _ n: Double) -> Double {
    return (P * V) / (R * n)
}

let OPTS = ["P", "V", "n", "R", "T"]

func getInputs(_ opt: String) -> [String: Double] {
    let idx = OPTS.firstIndex(of: opt)
    var active_opts = OPTS
    active_opts.remove(at: idx!)

    var inputs: [String: Double] = [:]

    for opt in active_opts {
        print("Enter \(opt)")
        let val = readLine()
        inputs[opt] = Double(val!)!
    }

    return inputs
}

func main() {
    print("What do you want to Calulate? (P, V, n, R, T)")
    let user_input = readLine()

    if user_input != nil, OPTS.contains(user_input!) {
        switch user_input! {
        case "R":
            print(R)
        case "P":
            let inputs = getInputs(user_input!)
            print(calculate_pressure(inputs["V"]!, inputs["n"]!, inputs["T"]!))
        case "V":
            let inputs = getInputs(user_input!)
            print(calculate_volume(inputs["P"]!, inputs["n"]!, inputs["T"]!))
        case "n":
            let inputs = getInputs(user_input!)
            print(calculate_moles(inputs["P"]!, inputs["V"]!, inputs["T"]!))
        case "T":
            let inputs = getInputs(user_input!)
            print(calculate_temprature(inputs["P"]!, inputs["V"]!, inputs["n"]!))
        default:
            print("Invalid")
        }
    } else {
        print("Invalid")
    }
}

main()
