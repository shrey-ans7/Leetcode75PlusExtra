import java.lang.*;
class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i=0; i<board.length; i++){
            Set<Character> hashSet = new HashSet<Character>();
            for(int j=0; j<board.length; j++) {
                if(Character.isDigit(board[i][j])){
                    if(!hashSet.contains(board[i][j])){
                        hashSet.add(board[i][j]);
                    }
                    else {
                        return false;
                    }
                } 
                
            }
        }
        for(int j=0; j<board.length; j++){
            Set<Character> hashSet = new HashSet<Character>();
            for(int i=0; i<board.length; i++) {
                if(Character.isDigit(board[i][j])){
                    if(!hashSet.contains(board[i][j])){
                        hashSet.add(board[i][j]);
                    }
                    else {
                        return false;
                    }
                } 
                
            }
        }
        
        for(int k=0; k<board.length; k+=3){
            for(int l=0; l<board.length; l+=3){
                Set<Character> hashSet = new HashSet<Character>();
                for( int i=k; i<k+3; i++){
                    for( int j=l; j<l+3; j++) {
                        if(Character.isDigit(board[i][j])){
                            if(!hashSet.contains(board[i][j])){
                                hashSet.add(board[i][j]);
                            }
                            else {
                                return false;
                            }
                        } 
                        
                    }
                }
            }
        }



        return true;
        
    }
}
