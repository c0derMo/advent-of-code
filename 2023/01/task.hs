module Task where
import Data.Char (isDigit, digitToInt)

taskOne :: [String] -> String
taskOne input = show (sum (map (addFirstAndLast . getAllNumbers) input))

taskTwo :: [String] -> String
taskTwo input = show (sum (map (addFirstAndLast . advancedParseDigit) input))

getAllNumbers :: String -> [Int]
getAllNumbers input = map digitToInt (filter isDigit input)

addFirstAndLast :: [Int] -> Int
addFirstAndLast input = head input * 10 + last input


advancedParseDigit :: String -> [Int]
advancedParseDigit input
    | null input = []
    | isDigit (head input) = digitToInt (head input) : advancedParseDigit (tail input)
    | subListAtStart "one" input = 1 : advancedParseDigit (tail input)
    | subListAtStart "two" input = 2 : advancedParseDigit (tail input)
    | subListAtStart "three" input = 3 : advancedParseDigit (tail input)
    | subListAtStart "four" input = 4 : advancedParseDigit (tail input)
    | subListAtStart "five" input = 5 : advancedParseDigit (tail input)
    | subListAtStart "six" input = 6 : advancedParseDigit (tail input)
    | subListAtStart "seven" input = 7 : advancedParseDigit (tail input)
    | subListAtStart "eight" input = 8 : advancedParseDigit (tail input)
    | subListAtStart "nine" input = 9 : advancedParseDigit (tail input)
    | otherwise = advancedParseDigit (tail input)


subListAtStart :: Eq a => [a] -> [a] -> Bool
subListAtStart [] [] = True
subListAtStart _ []    = False
subListAtStart [] _    = True
subListAtStart (x:xs) (y:ys) 
    | x == y    = subListAtStart xs ys   
    | otherwise = False