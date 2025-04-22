import tkinter as tk
from tkinter import messagebox, ttk
import math
from tkinter import font as tkfont

class SMOCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор СМО для автосервиса")
        self.root.geometry("600x500")
        self.root.configure(bg="#2c3e50")
        
        # Настройка стилей
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#2c3e50")
        self.style.configure("TLabel", background="#2c3e50", foreground="white", font=("Arial", 10))
        self.style.configure("Header.TLabel", font=("Arial", 16, "bold"), background="#2c3e50", foreground="#3498db")
        self.style.configure("Result.TLabel", font=("Arial", 10, "bold"), background="#2c3e50", foreground="#2ecc71")
        self.style.configure("Input.TLabel", font=("Arial", 10), background="#2c3e50", foreground="#ecf0f1")
        
        # Создание основного фрейма
        main_frame = ttk.Frame(root, style="TFrame", padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Заголовок
        header_label = ttk.Label(main_frame, 
                               text="Калькулятор системы массового обслуживания", 
                               style="Header.TLabel")
        header_label.pack(pady=(0, 20))
        
        # Подзаголовок
        subheader_label = ttk.Label(main_frame, 
                                  text="Расчет параметров автосервиса", 
                                  style="TLabel",
                                  font=("Arial", 12))
        subheader_label.pack(pady=(0, 20))
        
        # Создание фрейма для полей ввода
        input_frame = ttk.Frame(main_frame, style="TFrame")
        input_frame.pack(fill=tk.X, pady=10)
        
        # Стиль для полей ввода
        entry_style = ttk.Style()
        entry_style.configure("Custom.TEntry", 
                            fieldbackground="#34495e", 
                            foreground="white",
                            padding=5)
        
        # Поля ввода с улучшенным стилем
        # Интенсивность поступления
        lambda_frame = ttk.Frame(input_frame, style="TFrame")
        lambda_frame.pack(fill=tk.X, pady=5)
        ttk.Label(lambda_frame, 
                 text="Интенсивность поступления (λ, авто/час):", 
                 style="Input.TLabel").pack(side=tk.LEFT, padx=5)
        self.lambda_entry = tk.Entry(lambda_frame, 
                                   width=20,
                                   bg="#34495e",
                                   fg="white",
                                   font=("Arial", 10),
                                   insertbackground="white")
        self.lambda_entry.pack(side=tk.RIGHT, padx=5)
        
        # Интенсивность обслуживания
        mu_frame = ttk.Frame(input_frame, style="TFrame")
        mu_frame.pack(fill=tk.X, pady=5)
        ttk.Label(mu_frame, 
                 text="Интенсивность обслуживания (μ, авто/час):", 
                 style="Input.TLabel").pack(side=tk.LEFT, padx=5)
        self.mu_entry = tk.Entry(mu_frame, 
                               width=20,
                               bg="#34495e",
                               fg="white",
                               font=("Arial", 10),
                               insertbackground="white")
        self.mu_entry.pack(side=tk.RIGHT, padx=5)
        
        # Количество станций
        n_frame = ttk.Frame(input_frame, style="TFrame")
        n_frame.pack(fill=tk.X, pady=5)
        ttk.Label(n_frame, 
                 text="Количество станций (n, макс. 4):", 
                 style="Input.TLabel").pack(side=tk.LEFT, padx=5)
        self.n_entry = tk.Entry(n_frame, 
                              width=20,
                              bg="#34495e",
                              fg="white",
                              font=("Arial", 10),
                              insertbackground="white")
        self.n_entry.pack(side=tk.RIGHT, padx=5)
        
        # Кнопка расчета с улучшенным стилем
        calc_button = ttk.Button(main_frame, 
                               text="Рассчитать", 
                               command=self.calculate_smo, 
                               style="TButton")
        calc_button.pack(pady=20)
        
        # Создание фрейма для результатов
        result_frame = ttk.Frame(main_frame, style="TFrame")
        result_frame.pack(fill=tk.X, pady=10)
        
        # Поля вывода с улучшенным стилем
        # Вероятность отказа
        pref_frame = ttk.Frame(result_frame, style="TFrame")
        pref_frame.pack(fill=tk.X, pady=5)
        ttk.Label(pref_frame, 
                 text="Вероятность отказа (P_ref):", 
                 style="Input.TLabel").pack(side=tk.LEFT, padx=5)
        self.pref_label = ttk.Label(pref_frame, 
                                  text="", 
                                  style="Result.TLabel")
        self.pref_label.pack(side=tk.RIGHT, padx=5)
        
        # Относительная пропускная способность
        q_frame = ttk.Frame(result_frame, style="TFrame")
        q_frame.pack(fill=tk.X, pady=5)
        ttk.Label(q_frame, 
                 text="Относительная пропускная способность (Q):", 
                 style="Input.TLabel").pack(side=tk.LEFT, padx=5)
        self.q_label = ttk.Label(q_frame, 
                               text="", 
                               style="Result.TLabel")
        self.q_label.pack(side=tk.RIGHT, padx=5)
        
        # Абсолютная пропускная способность
        a_frame = ttk.Frame(result_frame, style="TFrame")
        a_frame.pack(fill=tk.X, pady=5)
        ttk.Label(a_frame, 
                 text="Абсолютная пропускная способность (A):", 
                 style="Input.TLabel").pack(side=tk.LEFT, padx=5)
        self.a_label = ttk.Label(a_frame, 
                               text="", 
                               style="Result.TLabel")
        self.a_label.pack(side=tk.RIGHT, padx=5)
        
        # Добавление информационного текста внизу
        info_text = "Этот калькулятор помогает оценить эффективность работы автосервиса,\n" \
                   "рассчитывая вероятность отказа, пропускную способность и другие параметры."
        info_label = ttk.Label(main_frame, 
                             text=info_text, 
                             style="TLabel", 
                             justify=tk.CENTER,
                             font=("Arial", 10, "italic"))
        info_label.pack(pady=20)
    
    def calculate_smo(self):
        try:
            # Получение и проверка входных данных
            lambda_val = float(self.lambda_entry.get())
            mu_val = float(self.mu_entry.get())
            n_val = int(self.n_entry.get())
            
            if lambda_val <= 0 or mu_val <= 0 or n_val <= 0:
                raise ValueError("Все значения должны быть положительными.")
            
            # Проверка максимального количества станций
            if n_val > 4:
                raise ValueError("Количество станций не может превышать 4.")
            
            # Расчет интенсивности трафика
            rho = lambda_val / mu_val
            
            # Расчет P_0 (нормализационная константа)
            sum_terms = sum((rho ** j) / math.factorial(j) for j in range(n_val + 1))
            p0 = 1 / sum_terms
            
            # Вероятность отказа (P_n)
            p_ref = ((rho ** n_val) / math.factorial(n_val)) * p0
            
            # Относительная пропускная способность
            q_val = 1 - p_ref
            
            # Абсолютная пропускная способность
            a_val = lambda_val * q_val
            
            # Обновление полей вывода
            self.pref_label.config(text=f"{p_ref:.4f}")
            self.q_label.config(text=f"{q_val:.4f}")
            self.a_label.config(text=f"{a_val:.2f} авто/час")
            
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", f"Некорректные данные: {e}")
        except Exception as e:
            messagebox.showerror("Ошибка расчета", f"Произошла ошибка: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SMOCalculator(root)
    root.mainloop() 