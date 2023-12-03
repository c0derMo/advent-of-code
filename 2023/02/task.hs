module Task where

taskOne :: [String] -> String
taskOne input = show (sum (map returnIdIfPossible (map (split (==':')) input)))

taskTwo :: [String] -> String
taskTwo input = show (sum (map gamePower (map (last . split (==':')) input)))


maxRed = 12
maxGreen = 13
maxBlue = 14


returnIdIfPossible :: [String] -> Int
returnIdIfPossible game
    | isGamePossible (tail (head (tail game))) = parseId (head game)
    | otherwise = 0


split     :: (Char -> Bool) -> String -> [String]
split p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : split p s''
                            where (w, s'') = break p s'

isGamePossible :: String -> Bool
isGamePossible game = all (== True) (map isShowPossible (split (==';') game))

isShowPossible :: String -> Bool
isShowPossible show = all (== True) (map isColorPossible (split (==',') show))

isColorPossible :: String -> Bool
isColorPossible colorThing
    | last (words colorThing) == "red" = read (head (words colorThing)) <= maxRed
    | last (words colorThing) == "green" = read (head (words colorThing)) <= maxGreen
    | last (words colorThing) == "blue" = read (head (words colorThing)) <= maxBlue
    | otherwise = True

parseId :: String -> Int
parseId title = read (last (words title))

gamePower :: String -> Int
gamePower game = minColorNeeded "red" game * minColorNeeded "green" game * minColorNeeded "blue" game

minColorNeeded :: String -> String -> Int
minColorNeeded color game = foldr (getMinColor color) 0 (flattenList (map (split (== ',')) (split (==';') game)))

getMinColor :: String -> String -> Int -> Int
getMinColor color currentShow prevMin
    | last (words currentShow) == color = max (read (head (words currentShow))) prevMin
    | otherwise = prevMin

flattenList :: [[a]] -> [a]
flattenList list = foldr (++) [] list