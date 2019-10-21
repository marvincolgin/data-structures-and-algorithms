package datastructs;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

import java.beans.Transient;
import java.util.function.BiFunction;
import java.util.function.Consumer;
import java.util.concurrent.atomic.AtomicReference;
import java.util.function.BiConsumer;

import datastructs.Stack;


public class StackTest {

   @Test
   public void testCountEmpty() {
      Stack s = new Stack();
      assertTrue(s.count()==0);
   }

   @Test
   public void testPush() {
      Stack s = new Stack();
      s.push("pao de queijo");
      assertTrue(s.count()==1);
   }

   @Test
   public void testStackPeek() {
      Stack s = helperStackAddLots();

      LinkList.RetObj retobj = s.peek();
      assertTrue(retobj.retBool==true);
      assertTrue(retobj.retVal=="banana");
   }

   @Test
   public void testPop() {
      Stack s = new Stack();
      s.push("a");
      String actual = s.pop();
      assertTrue(actual=="a");
   }

   private Stack helperStackAddLots() {
      Stack s = new Stack();
      s.push("pao de queijo");
      s.push("pappa sandwidh");
      s.push("banana");
      return s;
   }

   @Test
   public void testPushLots() {
      Stack s = helperStackAddLots();
      assertTrue(s.count()==3);
   }

   @Test
   public void testPopFromLots() {
      Stack s = helperStackAddLots();
      String actual = s.pop();
      assertTrue(actual=="banana");
      assertTrue(s.count()==2);
   }

   @Test
   public void testPopUntilEmpty() {
      Stack s = helperStackAddLots();

      // pop all but 1
      int len = s.count();
      for (int i=0; i<len-1; i++) {
         s.pop();
      }
      assertTrue(s.count()==1);

      // pop last one
      s.pop();
      assertTrue(s.count()==0);
   }

   @Test
   public void testToStr() {
      Stack s = helperStackAddLots();

      String[] arr = s.toStr().split(",");
      assertTrue(arr.length == 3);
   }

}
