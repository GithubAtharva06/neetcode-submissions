class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> string1 = new HashMap<>();
        Map<Character, Integer> string2 = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            int count = string1.getOrDefault(s.charAt(i), 0);
            count++;
            string1.put(s.charAt(i), count);
        }
        for(int i = 0; i < t.length(); i++){
            int count = string2.getOrDefault(t.charAt(i), 0);
            count++;
            string2.put(t.charAt(i), count);
        }
        if(string1.equals(string2)){
            return true;
        }
        else{
            return false;
        }
    }
}
