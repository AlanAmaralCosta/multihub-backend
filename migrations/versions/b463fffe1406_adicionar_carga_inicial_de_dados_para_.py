"""Adicionar carga inicial de dados para professional

Revision ID: b463fffe1406
Revises: e063a35aaa95
Create Date: 2023-05-22 14:30:29.133773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b463fffe1406'
down_revision = 'e063a35aaa95'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Comandos de migração existentes...

    # Adicione o código para carregar os dados iniciais
    op.execute(
        """
        INSERT INTO professional (name, project, responsable, work_experience, level, hour_value, salary, current_work, to_be_rated, data_created)
        VALUES
            ('Ala Costa', 'Projeto 1', 'Responsável 1', 5, 9.5, 50.0, 5000.0, 'Trabalho Atual', True, '2023-05-22'),
            ('Karine Faria', 'Projeto 2', 'Responsável 2', 3, 8.0, 40.0, 4000.0, 'Outro Trabalho', False, '2023-05-21'),
            ('João Silva', 'Projeto 3', 'Responsável 3', 2, 7.5, 35.0, 3500.0, 'Trabalho Anterior', False, '2023-05-20'),
            ('Maria Santos', 'Projeto 4', 'Responsável 4', 6, 9.0, 45.0, 4500.0, 'Trabalho Atual', True, '2023-05-19'),
            ('Pedro Pereira', 'Projeto 5', 'Responsável 5', 4, 8.5, 42.0, 4200.0, 'Outro Trabalho', False, '2023-05-18'),
            ('Ana Oliveira', 'Projeto 6', 'Responsável 6', 3, 8.0, 40.0, 4000.0, 'Trabalho Atual', True, '2023-05-17'),
            ('Ricardo Almeida', 'Projeto 7', 'Responsável 7', 2, 7.5, 35.0, 3500.0, 'Outro Trabalho', False, '2023-05-16'),
            ('Sara Costa', 'Projeto 8', 'Responsável 8', 5, 9.0, 45.0, 4500.0, 'Trabalho Atual', True, '2023-05-15'),
            ('Paulo Faria', 'Projeto 9', 'Responsável 9', 4, 8.5, 42.0, 4200.0, 'Outro Trabalho', False, '2023-05-14'),
            ('Mariana Silva', 'Projeto 10', 'Responsável 10', 3, 8.0, 40.0, 4000.0, 'Trabalho Atual', True, '2023-05-13'),
            ('Rui Santos', 'Projeto 11', 'Responsável 11', 2, 7.5, 35.0, 3500.0, 'Outro Trabalho', False, '2023-05-12'),
            ('Inês Pereira', 'Projeto 12', 'Responsável 12', 5, 9.0, 45.0, 4500.0, 'Trabalho Atual', True, '2023-05-11'),
            ('Fernando Oliveira', 'Projeto 13', 'Responsável 13', 4, 8.5, 42.0, 4200.0, 'Outro Trabalho', False, '2023-05-10'),
            ('Carla Almeida', 'Projeto 14', 'Responsável 14', 3, 8.0, 40.0, 4000.0, 'Trabalho Atual', True, '2023-05-09'),
            ('Hugo Costa', 'Projeto 15', 'Responsável 15', 2, 7.5, 35.0, 3500.0, 'Outro Trabalho', False, '2023-05-08'),
            ('Lúcia Faria', 'Projeto 16', 'Responsável 16', 5, 9.0, 45.0, 4500.0, 'Trabalho Atual', True, '2023-05-07'),
            ('Daniel Silva', 'Projeto 17', 'Responsável 17', 4, 8.5, 42.0, 4200.0, 'Outro Trabalho', False, '2023-05-06'),
            ('Rita Santos', 'Projeto 18', 'Responsável 18', 3, 8.0, 40.0, 4000.0, 'Trabalho Atual', True, '2023-05-05'),
            ('Miguel Pereira', 'Projeto 19', 'Responsável 19', 2, 7.5, 35.0, 3500.0, 'Outro Trabalho', False, '2023-05-04'),
            ('Teresa Oliveira', 'Projeto 20', 'Responsável 20', 5, 9.0, 45.0, 4500.0, 'Trabalho Atual', True, '2023-05-03')
        """
    )

    # Mais comandos de migração...


def downgrade() -> None:
    # Comandos de downgrade existentes...

    # Adicione o código para remover os dados iniciais
    op.execute("DELETE FROM professional")

    # Mais comandos de downgrade...