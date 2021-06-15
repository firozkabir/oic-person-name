create table person_name 
(
  sisid       number (9,0)         not null,
  dlc         date                 not null,
  surname     varchar2 (200)       not null,
  firstname   varchar2 (200)       not null,

  constraint pk_pn primary key (sisid)
);


create or replace procedure proc_person_name
(

    in_sisid     person_name.sisid%type,
    in_surname   person_name.surname%type,
    in_firstname person_name.firstname%type

)
as  pragma autonomous_transaction;
    v_count number := 0;
begin
    select count(*) into v_count
    from person_name
    where sisid = in_sisid;

    if v_count > 0 then 
        update person_name u 
        set u.dlc = sysdate,
            u.surname = in_surname,
            u.firstname = in_firstname
        where u.sisid = in_sisid;
    else
        insert into person_name (sisid, dlc, surname, firstname) values (in_sisid, sysdate, in_surname, in_firstname);
    end if;
    commit;

end;
/