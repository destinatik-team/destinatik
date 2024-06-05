package com.dicoding.destinatik

import android.content.Intent
import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.dicoding.destinatik.databinding.ActivityForgotPasswordBinding
import com.dicoding.destinatik.databinding.ActivityLoginBinding

class ForgotPasswordActivity : AppCompatActivity() {
    private var _binding: ActivityForgotPasswordBinding? = null
    private val binding get() = _binding!!
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        _binding = ActivityForgotPasswordBinding.inflate(layoutInflater)
        setContentView(binding.root)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        binding.apply {
            ivBackRegiser.setOnClickListener{
                val intent = Intent(this@ForgotPasswordActivity, LoginActivity::class.java)
                startActivity(intent)
            }
            tvLogin.setOnClickListener {
                val intent = Intent(this@ForgotPasswordActivity, LoginActivity::class.java)
                startActivity(intent)
            }
            RBtnVerify.setOnClickListener {
                val intent = Intent(this@ForgotPasswordActivity, VerifyActivity::class.java)
                startActivity(intent)
            }
        }
    }

}