public class firstBadVersion extends VersionControl {
    public int firstBadVersion(int n) {
        return binarySearch(1, n);
    }

    private int binarySearch(int s, int e){
        int firstBadVersion = e;
        while(s<=e){
            //(s+e)더했을 때, 오버플로우가 발생할 수 있음..; 
            int m = s + (e-s)/2;

            //bad Version이라면, 왼쪽에서 찾는다.
            if(isBadVersion(m)){
                e = m - 1;
                firstBadVersion = m;
            //bad Version이 아니라면, 오른쪽에서 찾는다.
            } else{
                s = m + 1;
            }
        }

        return firstBadVersion;
    }
}

class VersionControl{
    public isBadVersion(int num){

    }
} 

//2126753390
//1702766719