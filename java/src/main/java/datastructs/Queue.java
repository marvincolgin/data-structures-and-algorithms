package datastructs;

import java.util.function.BiFunction;
import java.util.function.Consumer;


import datastructs.LinkList;

public class Queue {
   private LinkList _data = null;

   public Queue() {
      this._data = new LinkList(null);
   }

   public int count() {
      return this._data.count();
   }

   public Boolean enqueue(String val) {
      this._data.append(val);
      return true;
   }

   public Boolean dequeue(String val) {
      return this._data.remove(val);
   }

   public LinkList.RetObj peek() {
      return this._data.peek();
   }

   public String toStr() {
      return this._data.toStr();
   }

}
