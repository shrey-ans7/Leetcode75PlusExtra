class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        
        int maxCandies=0;
        for (int numCandies: candies) {
            if (numCandies>maxCandies) maxCandies=numCandies;
        }
        List<Boolean> result = new ArrayList<Boolean>();

        for (int numCandies: candies) {
            if (numCandies+extraCandies>=maxCandies) result.add(true);
            else result.add(false);
        }
        return result;
    }
}
