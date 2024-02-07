import java.util.Scanner;
public class Priority_Queue {
    public static void main(String args[]){
        Scanner scan=new Scanner(System.in);
        String str="fnf";
        operations op=new operations();
        while(true){
            System.out.println("Enter what you need to do : enqueue-1 ,dequeue-2 , display-3, exit-4  :");
            str=scan.nextLine();
            if (str.equalsIgnoreCase("1")){
                System.out.println("Enter the value to add : ");
                int val=scan.nextInt();
                System.out.println("enter the priority : ");
                int pri=scan.nextInt();
                op.enqueue(val, pri);
                op.display();
            }
            else if(str.equalsIgnoreCase("2")){
                System.out.println(op.Dequeue());
            }
            else if(str.equals("4")){
                break;
            }
            else if (str.equals("3")){
                op.display();
            }
        }
        
    }
        
}
class Node{
    int value,priority;
    Node next;
    Node(int value,int priority){
        this.value=value;
        this.priority=priority;
        this.next=null;
    }
}
class operations{
    Node head,temp,add;
    operations(){
        this.head=null;
    }
    void enqueue(int v,int p){
        Node n=new Node(v,p);
        this.Queue(n);
    }
    void Queue(Node n){
        if (head==null){
            head=n;
        }
        else{
            temp=head;
            while(temp.next!=null){
                temp=temp.next;
            }
            temp.next=n;
        }
    }
    void delete_first(){
        head=head.next;
    }
    void delete_last(){
        temp=head;
        while(temp.next!=null){
            temp=temp.next;
        }
        temp.next=null;
    }
    int Dequeue(){
        if (head==null){
            System.out.println("Queue is empty ");
        }
        else{
            temp=head;
            int max=head.priority;
            while(temp.next!=null){
                if (max<temp.priority){
                    max=temp.priority;
                }
                temp=temp.next;
            }
            temp=head;
            while(temp.next!=null){
                if(max==temp.priority){
                    int a=temp.value;
                    if(temp==head){
                        delete_first();
                    }
                    else if(temp.next==null){
                        delete_last();
                    }
                    else{
                        add.next=temp.next;
                    }
                    return a;
                }
                add=temp;
                temp=temp.next;
            }
            if (head==temp){
                int b=temp.value;
                delete_first();
                return b;
            }
        }
        return -1;
    }
    void display(){
        temp=head;
        while(temp!=null){
            System.out.print(temp.value+"-->");
            temp=temp.next;
        }
    }
}
