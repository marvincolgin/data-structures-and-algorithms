package datastructs;

import org.junit.jupiter.api.Test;

import static java.lang.System.out;

import static org.junit.jupiter.api.Assertions.*;

import java.beans.Transient;
import java.util.function.BiFunction;
import java.util.function.Consumer;
import java.util.concurrent.atomic.AtomicReference;
import java.util.function.BiConsumer;

import datastructs.Queue;


public class QueueTest {

   @Test
   public void testCountEmpty() {
      Queue q = new Queue();
      assertTrue(q.count()==0);
   }

   public Queue helperEnqueueLots() {
      Queue q = new Queue();
      q.enqueue("pao de queijo");
      q.enqueue("pappa sandwidh");
      q.enqueue("banana");
      q.enqueue("crackers");
      q.enqueue("strawberries");
      q.enqueue("chocolate chips");
      return q;
   }

   @Test
   public void testEnqueue() {
      Queue q = new Queue();
      q.enqueue("pao de queijo");
      assertTrue(q.count()==1);
   }

   @Test
   public void testEnqueueLots() {
      Queue q = helperEnqueueLots();
      assertTrue(q.count()==6);
   }

   @Test
   public void testDequeueSuccess() {
      Queue q = helperEnqueueLots();
      assertTrue(q.dequeue("banana"));
      assertTrue(q.count()==5);
   }

   @Test
   public void testDequeueError() {
      Queue q = helperEnqueueLots();
      assertFalse(q.dequeue("somethingyouwontfind"));
      assertTrue(q.count()==6);
   }

   @Test
   public void testPeek() {
      Queue q = helperEnqueueLots();
      LinkList.RetObj retobj = q.peek();
      assertTrue(retobj.retBool);
      assertTrue(retobj.retVal == "pao de queijo");
   }

   @Test
   public void testPeekEmpty() {
      Queue q = new Queue();
      LinkList.RetObj retobj = q.peek();
      assertFalse(retobj.retBool);
      assertTrue(retobj.retVal == null);
   }

   @Test
   public void testDequeueUntilEmpty() {
      Queue q = helperEnqueueLots();
      String[] arr = q.toStr().split(",");
      for (int i=0, len=arr.length; i<len; i++) {
         q.dequeue(arr[i]);
      }
      assertTrue(q.count()==0);
   }
}
