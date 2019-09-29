package datastructs;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

import datastructs.LinkList;


public class LinkListTest {
    @Test
    public void testLinkedListEmpty() {
        LinkList classUnderTest = new LinkList();
        LinkList.LinkNode expectedOutput = null;
        LinkList.LinkNode outputRecieved = classUnderTest.head;
        assertNull(expectedOutput, "There should be nothing in the list!");
    }
}