"""add_professional_table

Revision ID: 503752ce9360
Revises: b463fffe1406
Create Date: 2023-05-23 15:06:07.958310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '503752ce9360'
down_revision = 'b463fffe1406'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('professional', sa.Column('responsible', sa.String(), nullable=True))
    op.alter_column('professional', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('professional', 'project',
               existing_type=sa.VARCHAR(length=180),
               nullable=True)
    op.alter_column('professional', 'work_experience',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('professional', 'current_work',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('professional', 'to_be_rated',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('professional', 'data_created',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
    op.drop_column('professional', 'responsable')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('professional', sa.Column('responsable', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.alter_column('professional', 'data_created',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
    op.alter_column('professional', 'to_be_rated',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('professional', 'current_work',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('professional', 'work_experience',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('professional', 'project',
               existing_type=sa.VARCHAR(length=180),
               nullable=False)
    op.alter_column('professional', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.drop_column('professional', 'responsible')
    # ### end Alembic commands ###