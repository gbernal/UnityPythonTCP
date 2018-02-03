using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class InputString : MonoBehaviour {

    public GUIText gt;

    void Start()
    {
        gt = GetComponent<GUIText>();
    }

    void Update()
    {
        foreach (char c in Input.inputString)
        {
            if (c == '\b') // has backspace/delete been pressed?
            {
                if (gt.text.Length != 0)
                {
                    gt.text = gt.text.Substring(0, gt.text.Length - 1);
                }
            }
            else if ((c == '\n') || (c == '\r')) // enter/return
            {
                print("User entered their name: " + gt.text);
            }
            else
            {
                gt.text += c;
            }
        }
    }
}
