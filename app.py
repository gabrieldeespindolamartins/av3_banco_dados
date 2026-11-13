"""Mini aplicação desktop - Banco de Dados I - FMP.

VERSÃO DOS ALUNOS.

A interface é fornecida como apoio para que o foco permaneça em Banco de Dados.
Um fluxo completo de INSERT está pronto como exemplo.
As demais funcionalidades dependem dos TODOs de repositories.py.
"""

from __future__ import annotations

from datetime import date, datetime
import tkinter as tk
from tkinter import messagebox, ttk

from psycopg import Error as PsycopgError

import repositories as repo


def parse_date(value: str, required: bool = False) -> date | None:
    value = value.strip()
    if not value:
        if required:
            raise ValueError("Informe uma data no formato AAAA-MM-DD.")
        return None
    return datetime.strptime(value, "%Y-%m-%d").date()


def selected_id(combo_value: str) -> int | None:
    if not combo_value.strip():
        return None
    return int(combo_value.split(" - ", 1)[0])


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Projeto Final - Banco de Dados I - FMP - Versão Alunos")
        self.geometry("1120x700")
        self.minsize(980, 620)

        self.city_by_id: dict[int, str] = {}
        self.student_by_id: dict[int, str] = {}
        self.course_by_id: dict[int, str] = {}

        self._build_ui()
        self.load_reference_data()

    def _build_ui(self) -> None:
        title = ttk.Label(
            self,
            text="Mini Sistema Acadêmico FMP - Projeto Final",
            font=("Segoe UI", 17, "bold"),
        )
        title.pack(pady=(14, 2))

        ttk.Label(
            self,
            text="Versão dos alunos: complete os TODOs de SQL e repositories.py.",
        ).pack(pady=(0, 8))

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=14, pady=(0, 14))

        self.tab_students = ttk.Frame(notebook, padding=12)
        self.tab_enrollments = ttk.Frame(notebook, padding=12)
        self.tab_reports = ttk.Frame(notebook, padding=12)

        notebook.add(self.tab_students, text="Alunos - CRUD")
        notebook.add(self.tab_enrollments, text="Matrículas")
        notebook.add(self.tab_reports, text="Consulta / Relatório")

        self._build_students_tab()
        self._build_enrollments_tab()
        self._build_reports_tab()

    def _build_students_tab(self) -> None:
        form = ttk.LabelFrame(self.tab_students, text="Dados do aluno", padding=10)
        form.pack(fill="x")

        self.student_id = tk.StringVar()
        self.student_name = tk.StringVar()
        self.student_email = tk.StringVar()
        self.student_birth = tk.StringVar()
        self.student_city = tk.StringVar()

        fields = [
            ("ID", self.student_id, 10),
            ("Nome", self.student_name, 34),
            ("E-mail", self.student_email, 34),
            ("Nascimento (AAAA-MM-DD)", self.student_birth, 18),
        ]
        for col, (label, var, width) in enumerate(fields):
            ttk.Label(form, text=label).grid(row=0, column=col, sticky="w", padx=4)
            state = "readonly" if label == "ID" else "normal"
            ttk.Entry(form, textvariable=var, width=width, state=state).grid(
                row=1, column=col, sticky="ew", padx=4, pady=(2, 6)
            )

        ttk.Label(form, text="Cidade").grid(row=2, column=0, sticky="w", padx=4)
        self.city_combo = ttk.Combobox(
            form, textvariable=self.student_city, state="readonly", width=31
        )
        self.city_combo.grid(row=3, column=0, columnspan=2, sticky="w", padx=4)

        buttons = ttk.Frame(form)
        buttons.grid(row=3, column=2, columnspan=2, sticky="e")
        ttk.Button(buttons, text="Novo", command=self.clear_student_form).pack(side="left", padx=3)
        ttk.Button(buttons, text="Cadastrar", command=self.add_student).pack(side="left", padx=3)
        ttk.Button(buttons, text="Listar", command=self.load_students).pack(side="left", padx=3)
        ttk.Button(buttons, text="Atualizar", command=self.update_student).pack(side="left", padx=3)
        ttk.Button(buttons, text="Excluir", command=self.delete_student).pack(side="left", padx=3)

        cols = ("id", "nome", "email", "nascimento", "cidade")
        self.student_tree = ttk.Treeview(
            self.tab_students, columns=cols, show="headings", height=18
        )
        headings = {
            "id": "ID",
            "nome": "Nome",
            "email": "E-mail",
            "nascimento": "Nascimento",
            "cidade": "Cidade",
        }
        widths = {
            "id": 60,
            "nome": 220,
            "email": 280,
            "nascimento": 120,
            "cidade": 190,
        }
        for c in cols:
            self.student_tree.heading(c, text=headings[c])
            self.student_tree.column(c, width=widths[c], anchor="w")
        self.student_tree.pack(fill="both", expand=True, pady=(12, 0))
        self.student_tree.bind("<<TreeviewSelect>>", self.on_student_select)

    def _build_enrollments_tab(self) -> None:
        form = ttk.LabelFrame(self.tab_enrollments, text="Matrícula", padding=10)
        form.pack(fill="x")

        self.enroll_student = tk.StringVar()
        self.enroll_course = tk.StringVar()
        self.enroll_date = tk.StringVar(value=date.today().isoformat())

        ttk.Label(form, text="Aluno").grid(row=0, column=0, sticky="w", padx=4)
        self.enroll_student_combo = ttk.Combobox(
            form, textvariable=self.enroll_student, state="readonly", width=38
        )
        self.enroll_student_combo.grid(row=1, column=0, padx=4, sticky="w")

        ttk.Label(form, text="Curso").grid(row=0, column=1, sticky="w", padx=4)
        self.enroll_course_combo = ttk.Combobox(
            form, textvariable=self.enroll_course, state="readonly", width=46
        )
        self.enroll_course_combo.grid(row=1, column=1, padx=4, sticky="w")

        ttk.Label(form, text="Data (AAAA-MM-DD)").grid(row=0, column=2, sticky="w", padx=4)
        ttk.Entry(form, textvariable=self.enroll_date, width=17).grid(row=1, column=2, padx=4)

        buttons = ttk.Frame(form)
        buttons.grid(row=1, column=3, padx=5)
        ttk.Button(buttons, text="Matricular", command=self.add_enrollment).pack(side="left", padx=3)
        ttk.Button(buttons, text="Atualizar data", command=self.update_enrollment).pack(side="left", padx=3)
        ttk.Button(buttons, text="Excluir", command=self.delete_enrollment).pack(side="left", padx=3)
        ttk.Button(buttons, text="Listar JOIN", command=self.load_enrollments).pack(side="left", padx=3)

        cols = ("id_aluno", "aluno", "id_curso", "curso", "data", "cidade")
        self.enrollment_tree = ttk.Treeview(
            self.tab_enrollments, columns=cols, show="headings", height=19
        )
        labels = {
            "id_aluno": "ID Aluno",
            "aluno": "Aluno",
            "id_curso": "ID Curso",
            "curso": "Curso",
            "data": "Data",
            "cidade": "Cidade",
        }
        widths = {
            "id_aluno": 80,
            "aluno": 220,
            "id_curso": 80,
            "curso": 240,
            "data": 110,
            "cidade": 180,
        }
        for c in cols:
            self.enrollment_tree.heading(c, text=labels[c])
            self.enrollment_tree.column(c, width=widths[c], anchor="w")
        self.enrollment_tree.pack(fill="both", expand=True, pady=(12, 0))
        self.enrollment_tree.bind("<<TreeviewSelect>>", self.on_enrollment_select)

    def _build_reports_tab(self) -> None:
        top = ttk.Frame(self.tab_reports)
        top.pack(fill="x")
        ttk.Label(
            top,
            text="Consulta de negócio: quantidade de alunos por curso",
            font=("Segoe UI", 12, "bold"),
        ).pack(side="left")
        ttk.Button(top, text="Executar relatório", command=self.load_report).pack(side="right")

        cols = ("sigla", "curso", "total")
        self.report_tree = ttk.Treeview(
            self.tab_reports, columns=cols, show="headings", height=20
        )
        self.report_tree.heading("sigla", text="Sigla")
        self.report_tree.heading("curso", text="Curso")
        self.report_tree.heading("total", text="Total de alunos")
        self.report_tree.column("sigla", width=100)
        self.report_tree.column("curso", width=430)
        self.report_tree.column("total", width=140, anchor="center")
        self.report_tree.pack(fill="both", expand=True, pady=(12, 0))

    def _todo_message(self, exc: NotImplementedError) -> None:
        messagebox.showwarning(
            "Funcionalidade a desenvolver",
            str(exc) + "\n\nConsulte repositories.py e o roteiro do projeto.",
        )

    def load_reference_data(self) -> None:
        """Carrega somente dados de referência que já possuem SELECT de exemplo."""
        try:
            cities = repo.listar_cidades()
            courses = repo.listar_cursos()

            city_values = []
            self.city_by_id.clear()
            for row in cities:
                label = f"{row['id_cidade']} - {row['nome']}/{row['uf']}"
                self.city_by_id[row["id_cidade"]] = label
                city_values.append(label)
            self.city_combo["values"] = city_values

            course_values = []
            self.course_by_id.clear()
            for row in courses:
                label = f"{row['id_curso']} - {row['sigla']} - {row['nome']}"
                self.course_by_id[row["id_curso"]] = label
                course_values.append(label)
            self.enroll_course_combo["values"] = course_values
        except PsycopgError as exc:
            messagebox.showerror(
                "Banco não preparado",
                "Não foi possível carregar cidades/cursos.\n\n"
                "Conclua 01_schema.sql, execute 02_seed.sql e confira a conexão.\n\n"
                f"Detalhe: {exc}",
            )

    def validate_student(self) -> tuple[str, str, date | None, int | None]:
        name = self.student_name.get().strip()
        email = self.student_email.get().strip()
        if not name:
            raise ValueError("Informe o nome.")
        if "@" not in email:
            raise ValueError("Informe um e-mail válido.")
        birth = parse_date(self.student_birth.get())
        city_id = selected_id(self.student_city.get())
        return name, email, birth, city_id

    # ========================================================
    # EXEMPLO COMPLETO: botão -> validação -> INSERT -> banco
    # ========================================================
    def add_student(self) -> None:
        try:
            repo.inserir_aluno(*self.validate_student())
            self.clear_student_form()
            messagebox.showinfo(
                "Sucesso",
                "Aluno cadastrado no PostgreSQL.\n\n"
                "Agora implemente TODO 5 para que o botão Listar exiba os alunos.",
            )
        except (ValueError, PsycopgError) as exc:
            messagebox.showerror("Não foi possível cadastrar", str(exc))

    def load_students(self) -> None:
        try:
            rows = repo.listar_alunos()
        except NotImplementedError as exc:
            self._todo_message(exc)
            return
        except PsycopgError as exc:
            messagebox.showerror("Erro ao consultar", str(exc))
            return

        for item in self.student_tree.get_children():
            self.student_tree.delete(item)

        self.student_by_id.clear()
        student_combo = []
        for row in rows:
            city = ""
            if row.get("cidade"):
                city = f"{row['cidade']}/{row.get('uf', '')}".rstrip("/")
            birth = row["data_nascimento"].isoformat() if row.get("data_nascimento") else ""
            self.student_tree.insert(
                "", "end",
                values=(row["id_aluno"], row["nome"], row["email"], birth, city),
                tags=(str(row.get("id_cidade") or ""),),
            )
            label = f"{row['id_aluno']} - {row['nome']}"
            self.student_by_id[row["id_aluno"]] = label
            student_combo.append(label)

        self.enroll_student_combo["values"] = student_combo

    def update_student(self) -> None:
        if not self.student_id.get():
            messagebox.showwarning("Seleção", "Selecione um aluno na tabela.")
            return
        try:
            repo.atualizar_aluno(int(self.student_id.get()), *self.validate_student())
            self.load_students()
            messagebox.showinfo("Sucesso", "Aluno atualizado.")
        except NotImplementedError as exc:
            self._todo_message(exc)
        except (ValueError, PsycopgError) as exc:
            messagebox.showerror("Não foi possível atualizar", str(exc))

    def delete_student(self) -> None:
        if not self.student_id.get():
            messagebox.showwarning("Seleção", "Selecione um aluno na tabela.")
            return
        if not messagebox.askyesno("Confirmar", "Excluir o aluno selecionado?"):
            return
        try:
            repo.excluir_aluno(int(self.student_id.get()))
            self.clear_student_form()
            self.load_students()
        except NotImplementedError as exc:
            self._todo_message(exc)
        except PsycopgError as exc:
            messagebox.showerror("Não foi possível excluir", str(exc))

    def clear_student_form(self) -> None:
        self.student_id.set("")
        self.student_name.set("")
        self.student_email.set("")
        self.student_birth.set("")
        self.student_city.set("")

    def on_student_select(self, _event: object) -> None:
        selected = self.student_tree.selection()
        if not selected:
            return
        values = self.student_tree.item(selected[0], "values")
        tags = self.student_tree.item(selected[0], "tags")
        self.student_id.set(values[0])
        self.student_name.set(values[1])
        self.student_email.set(values[2])
        self.student_birth.set(values[3])
        city_id = int(tags[0]) if tags and tags[0] else None
        self.student_city.set(self.city_by_id.get(city_id, ""))

    def enrollment_values(self) -> tuple[int, int, date]:
        student_id = selected_id(self.enroll_student.get())
        course_id = selected_id(self.enroll_course.get())
        if student_id is None or course_id is None:
            raise ValueError("Selecione o aluno e o curso.")
        enroll_date = parse_date(self.enroll_date.get(), required=True)
        assert enroll_date is not None
        return student_id, course_id, enroll_date

    def add_enrollment(self) -> None:
        try:
            repo.inserir_matricula(*self.enrollment_values())
            self.load_enrollments()
        except NotImplementedError as exc:
            self._todo_message(exc)
        except (ValueError, PsycopgError) as exc:
            messagebox.showerror("Não foi possível matricular", str(exc))

    def update_enrollment(self) -> None:
        try:
            student_id, course_id, enroll_date = self.enrollment_values()
            repo.atualizar_data_matricula(student_id, course_id, enroll_date)
            self.load_enrollments()
        except NotImplementedError as exc:
            self._todo_message(exc)
        except (ValueError, PsycopgError) as exc:
            messagebox.showerror("Não foi possível atualizar", str(exc))

    def delete_enrollment(self) -> None:
        try:
            student_id, course_id, _ = self.enrollment_values()
            repo.excluir_matricula(student_id, course_id)
            self.load_enrollments()
        except NotImplementedError as exc:
            self._todo_message(exc)
        except (ValueError, PsycopgError) as exc:
            messagebox.showerror("Não foi possível excluir", str(exc))

    def load_enrollments(self) -> None:
        try:
            rows = repo.listar_matriculas()
        except NotImplementedError as exc:
            self._todo_message(exc)
            return
        except PsycopgError as exc:
            messagebox.showerror("Erro no JOIN", str(exc))
            return

        for item in self.enrollment_tree.get_children():
            self.enrollment_tree.delete(item)

        for row in rows:
            self.enrollment_tree.insert(
                "", "end",
                values=(
                    row["id_aluno"],
                    row["aluno"],
                    row["id_curso"],
                    f"{row['sigla']} - {row['curso']}",
                    row["data_matricula"],
                    row.get("cidade") or "",
                ),
            )

    def on_enrollment_select(self, _event: object) -> None:
        selected = self.enrollment_tree.selection()
        if not selected:
            return
        values = self.enrollment_tree.item(selected[0], "values")
        student_id = int(values[0])
        course_id = int(values[2])
        self.enroll_student.set(self.student_by_id.get(student_id, f"{student_id} - ?"))
        self.enroll_course.set(self.course_by_id.get(course_id, f"{course_id} - ?"))
        self.enroll_date.set(values[4])

    def load_report(self) -> None:
        try:
            rows = repo.resumo_por_curso()
        except NotImplementedError as exc:
            self._todo_message(exc)
            return
        except PsycopgError as exc:
            messagebox.showerror("Erro no relatório", str(exc))
            return

        for item in self.report_tree.get_children():
            self.report_tree.delete(item)

        for row in rows:
            self.report_tree.insert(
                "", "end",
                values=(row["sigla"], row["curso"], row["total_alunos"]),
            )


if __name__ == "__main__":
    App().mainloop()
