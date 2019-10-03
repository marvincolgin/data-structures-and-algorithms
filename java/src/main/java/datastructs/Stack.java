package datastructs;

import java.util.function.BiFunction;
import java.util.function.Consumer;


import datastructs.LinkList;


public class Stack {
   private LinkList _data = null;

   public Stack() {
      this._data = new LinkList(null);
   }

   public int count() {
      return this._data.count();
   }

   public Boolean push(String val) {
      this._data.insert(val);
      return true;
   }

   public String pop() {
      LinkList.RetObj retobj = this._data.peek();
      if (!retobj.retBool) {
         return new String("");
      }

      this._data.remove(retobj.retVal);
      return retobj.retVal;
   }

   public LinkList.RetObj peek() {
      return this._data.peek();
   }

}
