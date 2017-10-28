disemvowel :: String -> (String, String)
disemvowel str = 
      let con = filter (\c -> not $ c `elem` vowels) str
          vow = filter (\c -> c `elem` vowels) str
          vowels = ['a', 'e', 'i', 'o', 'u']
      in  (con, vow)