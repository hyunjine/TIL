package com.example.playground

import kotlinx.coroutines.CoroutineExceptionHandler
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import org.junit.Test

import org.junit.Assert.*
import kotlin.system.measureTimeMillis

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * See [testing documentation](http://d.android.com/tools/testing).
 */
class ExampleUnitTest {
    private val exceptionHandler = CoroutineExceptionHandler { _, throwable ->
        // Handle the exception
        throwable.printStackTrace()
    }

    // Create a CoroutineScope with the exception handler and Main dispatcher
    private val coroutineScope = CoroutineScope(Dispatchers.Main + exceptionHandler)

    @Test
    // Function to perform a network request using a coroutine
    fun performNetworkRequest() {
        coroutineScope.launch {
            try {
                getM()
            } catch (e: Exception) {
                println(e)
                // Handle the network error here
            }
        }
    }

    suspend fun getM() {
        throw java.lang.Exception()
    }
}