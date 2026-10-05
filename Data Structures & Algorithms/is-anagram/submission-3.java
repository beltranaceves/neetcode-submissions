class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> refS = new HashMap<>();
        HashMap<Character, Integer> refT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char key = s.charAt(i);
            if (refS.containsKey(key)) {
                int value = refS.get(key) + 1;
                refS.put(key, value);
            } else {
                refS.put(key, 1);
            }
        }

        for (int i = 0; i < t.length(); i++) {
            char key = t.charAt(i);
            if (refT.containsKey(key)) {
                int value = refT.get(key) + 1;
                refT.put(key, value);
            } else {
                refT.put(key, 1);
            }
        }
        // System.out.println(refS);
        // System.out.println(refT);
        return refS.equals(refT);
    }
}
