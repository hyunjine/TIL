package com.example.playground

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.playground.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private val binding: ActivityMainBinding by lazy { ActivityMainBinding.inflate(layoutInflater) }
    
    private val num1: String
        get() = binding.edtNum1.text.toString()
    private val num2: String
        get() = binding.edtNum2.text.toString()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)
        setEvent()
    }
    
    private fun setEvent() = binding.run {
        btnPlus.setOnClickListener {
            checkEditTextValid { n1, n2 ->
                setDataText("${n1.plus(n2)}")
            }
        }
        btnMinus.setOnClickListener {
            checkEditTextValid { n1, n2 ->
                setDataText("${n1.minus(n2)}")
            }
        }
        btnTime.setOnClickListener {
            checkEditTextValid { n1, n2 ->
                setDataText("${n1.times(n2)}")
            }
        }
        btnDivide.setOnClickListener {
            checkEditTextValid { n1, n2 ->
                setDataText("${n1.div(n2)}")
            }
        }
    }
    
    private fun checkEditTextValid(callback: (Int, Int) -> Unit) {
        if (num1.isNotBlank() && num2.isNotBlank()) {
            callback(num1.toInt(), num2.toInt())
        }
    }

    private fun setDataText(text: String) {
        binding.tvData.text = text
    }
}