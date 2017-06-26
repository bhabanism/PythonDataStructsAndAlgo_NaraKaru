public class cellsJ {
   static int rows = 5;
   static int cols = 5;
   public static void main(String[] args) {

      int a[][] = new int[][] { 
         {1,1,0,0,0},
         {0,1,1,0,0},
         {0,0,1,0,1},
         {1,0,0,0,1},
         {0,1,0,1,1} 
      };

      printArray(a);
      int maxlength = scanArrayForConnections(a);
      System.out.println("Max length by rough scan is :" + maxlength );
   }

   private static int scanArrayForConnections(int[][] a) {
      int length = 0;
      int maxlength = 0;

      int i = 0, j = 0;
      while(i < rows) {
         while(j < rows) {
            if(a[i][j]==1) {
               length++;
            } 
            
            if(length > maxlength) {
               maxlength = length;
            }            

            if( j + 1 < cols && a[i][j+1] == 1) {
               j++;
            } else if( i + 1 < rows && a[i+1][j]==1) {
               i++;
            } else if(i + 1 < rows ){
               i++;
               j=0;
               length = 0; 
            } else {
               length = 0;
               return maxlength;
            }
         }
      }      
      return maxlength;
   }

   private static void printArray(int arr[][]) {
      for(int i = 0 ; i < rows; i++) {
         for(int j = 0 ; j < cols; j++) {
            System.out.print(arr[i][j] + " ");         
         }
         System.out.println("\n");
      }
   }
}
