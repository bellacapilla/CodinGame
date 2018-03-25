// Converts string to binary sequence of 7-bit
let stringToBin (msg: string) =
    let finalVerification (str:string) =
        if str.Length <= 6 then
            let newStr = String.replicate (7 - str.Length) "0"
            newStr + str
        else str
    
    let rec intToBin a =
        match a with
        |0 -> string a
        |1 -> string a
        |_ -> (intToBin (a/2)) + (string (a % 2))

    msg |> (Seq.map (fun x -> int x)) |> Seq.map intToBin |> String.concat "" |> finalVerification

// Returns a unary string
let binToChuck(binString: string) =
    let rec innerFun (i: int) (acc: int) (newString: string) =
        if i < (binString.Length-1) then
            if binString.[i] = '1' then
                if binString.[i+1] = '0' then
                    innerFun (i+1) 0 (newString + "0" + " " + (String.replicate (acc+1) "0") + " ")
                else
                    innerFun (i+1) (acc+1) newString

            else
                if binString.[i+1] = '1' then
                    innerFun (i+1) 0 (newString + "00" + " " + (String.replicate (acc + 1) "0") + " ")
                else
                    innerFun (i+1) (acc+1) newString

        else
            if binString.[i] = '1' then
                if (acc = 0) then
                    String.concat "" [(newString + "0 0")]
                else
                    String.concat "" [newString + "0" + " " + (String.replicate (acc + 1) "0")]

            else
                if (acc = 0) then                    
                    String.concat "" [(newString + "00 0")]
                else
                    String.concat "" [newString + "00" + " " + (String.replicate (acc + 1) "0")]

    innerFun 0 0 ""
