package com.msp1974.vacompanion.utils

import timber.log.Timber

class Logger {
    companion object {
        const val TAG = "ViewAssistCA"
    }
    fun d(message: String) {
        Timber.d(message)
    }
    fun e(message: String) {
        Timber.e(message)
    }
    fun i(message: String) {
        Timber.i(message)
    }
    fun w(message: String) {
        Timber.w(message)
    }
}
