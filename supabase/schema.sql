-- Ariane : schéma Supabase minimal pour les comptes et la sauvegarde en ligne.
--
-- À exécuter une seule fois dans l'éditeur SQL du projet Supabase
-- (https://app.supabase.com > ton projet > SQL Editor > New query > coller > Run).
--
-- Ne touche pas à l'authentification elle-même (table auth.users) : elle est
-- gérée entièrement par Supabase Auth. Ici on crée juste la table qui stocke
-- la sauvegarde JSON de chaque vendeur, avec des règles qui empêchent un
-- vendeur de lire ou modifier les données d'un autre.

create table if not exists public.ariane_data (
  user_id uuid primary key references auth.users(id) on delete cascade,
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

alter table public.ariane_data enable row level security;

create policy "Un vendeur lit ses propres données"
  on public.ariane_data for select
  using (auth.uid() = user_id);

create policy "Un vendeur crée ses propres données"
  on public.ariane_data for insert
  with check (auth.uid() = user_id);

create policy "Un vendeur met à jour ses propres données"
  on public.ariane_data for update
  using (auth.uid() = user_id)
  with check (auth.uid() = user_id);

create policy "Un vendeur supprime ses propres données"
  on public.ariane_data for delete
  using (auth.uid() = user_id);

-- Accès explicite via l'API (le projet n'expose pas automatiquement les
-- nouvelles tables). Seuls les utilisateurs connectés y ont droit, et les
-- règles RLS ci-dessus limitent chacun à sa propre ligne.
grant select, insert, update, delete on public.ariane_data to authenticated;
revoke all on public.ariane_data from anon;
