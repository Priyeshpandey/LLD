# Design a Movie Ticket application for a Theatre

# Requirements
1. A THEATRE has SCREENS to show MOVIES, they have show timing i.e date time
2. A Screen has AUDI/HALL with a seating arrangements.
3. We have a BookingSession for a user to book tickets
1. In a Session, user should be allowed to select a group of seats from AVAILABLE seats for a given screening.
1. During the BookingSession selected seats should be marked temporarily_unavailable in the system for other users.
1. If payment is success, issue ticket to the user and mark the seats permanently unavailable for other users.
1. If payment is failed, user should be able to retry payment for MAX number of times, afte MAX the temporarily_unavailable seats are made available again.
1. User can explicitly close a bookingSession at any point of time, while btrowsing seats, selecting seats, payment.

# Actors
1. Customers : People who uses this application to book ticket
1. Theatre Manager: Person who creates/updates/View/Remove Screening, view bookings for a screening.


Entities (Classes)
=========================================================
1. Theatre
    1. id : int
    2. name : string
    3. screens: List[Screen]
    ---
    + add_screen(screen: Screen)
    + remove_screen(screen: Screen)

2. Screen
    1. id: int
    2. theatre: Theatre (F.K) // has a theatre
    3. name: string
    4. seats: List[Seat]
    ---
    add_seat()
    remove_seat() 

3. Seat
    1. id: int
    2. row_number: int //bottom to top
    3. seat_number: int //Left to Right
    4. type: Enum {ECONOMY, PREMIUM, VIP} 

4. SeatLock:
    1. seat: Seat
    1. show: Show
    1. locked_at: DateAndTime
    1. timeout_in_seconds: int
    1. locked_by: User
    ---
    is_lock_expired()

5. Show:
    1. id: int
    3. movie: Movie
    4. start: Time
    5. duration_in_seconds: int
    6. date: Date
    8. screen: Screen
     
6. Booking
    1. id: int
    1. show: Show
    1. booked_by: User
    1. booked_at: Date&Time
    1. seats_booked: List[Seat]
    1. status: Enum {Confirmed, Expired, Created}
    ---
    is_booking_confirmed()
    confirm_booking()
    expire_booking()

7. Movie
    1. title: string
    2. id: int
    3. rating: Enum {POOR, BAD, AVERAGE, GOOD, BEST}


===================
Database Design (RDBMS like MySQL)

Movie (id(int), title(varchar), rating(0,1,2,3,4,5 : Enum)) : pk: id
Theatre (id(int), name: (varchar))
Screens (id(int), theatre (f.k: theatre_id), name(varchar))
Seat (id(int), row(int), col(int), type(enum: 0,1,2,3), screen:(screen_id: f.k))
SeatLock (id(int), seat(f.k: seat_id), show(show_id, f.k), locked_at(datetime| nullable), timeout(s), locked_by(user_id | f.k))
Show (id(int), movie_id(Movie), screen_id(Screen), start, duration, date)
Booking (id(int), show_id(Show), booked_by(user_id), booked_at, status)
BookedSeat (id, seat_id, booking_id)

=============================
Utils
----------------
SeatLockProvider (Interface)
    + lock_seat (show: Show, seat: Seat, user: User)
    + unlock_seat (show: Show, seat: Seat, user: User)
    + validate_lock (show: Show, seat: Seat, user: User)
    + get_locked_seats(show: Show)

InMemorySeatLockProvider : When saving locks in memory
DBSeatLockProvider: When using database to store locks

===============================
APIs (Business Logic)
------------------
TheatreController:
    - theatre_service: TheatreService
    ---
    + create_theatre(theatre_name: string) -> string // theatre_id
    + create_screen_in_theatre()
    + create_seat_in_screen()

MovieController :
    - movie_service: MovieService
    ---
    + create_movie()

BookingController:
    - booking_service: BookingService
    - show_service: ShowService
    - theatre_service: TheatreService
    ---
    + create_booking(user, show, seats)

ShowController :
    private final SeatAvailabilityService seatAvailabilityService;
    private final ShowService showService;
    private final TheatreService theatreService;
    private final MovieService movieService;
    ---
    public String createShow(@NonNull final String movieId, @NonNull final String screenId, @NonNull final Date startTime,
                             @NonNull final Integer durationInSeconds)
    public List<String> getAvailableSeats(@NonNull final String showId)

PaymentsController:
    private final PaymentsService paymentsService;
    private final BookingService bookingService;
    ---
    public void paymentFailed(@NonNull final String bookingId, @NonNull final String user)
    public void paymentSuccess(@NonNull final  String bookingId, @NonNull final String user)

Services
-------------
TheatreService:
    - theatres: Dict[string, Theatre]
    - screens: Dict[string, Screen]
    - seats: Dict[string, Seat]
    ---
    + create_theatre()
    + create_screen_in_theatre()
    + create_seat_in_screen()
    + create_screen()
    
MovieService:
    - movies: Dict[string, Movie]
    ---
    create_movie(title: string) -> Movie

ShowService:
    - shows: Dict[string, Show]
    ---
    + create_show()
    + get_shows_for_screen()
    + check_if_create_show_allowed_for_a_screen()

BookingService:
    - show_bookings: Dict[string, Booking]
    - seat_lock: SeatLockProvider
    ---
    + get_booking(booking_id: str) -> Booking
    + get_all_bookings(show: Show) -> List[Booking]
    + create_booking(user_id: str, show: Show, seats: List[Seat]) -> Booking
    + get_booked_seats(show: Show) -> List[Seat]
    + confirm_booking(booking: Booking, user: User) -> bool
    + is_any_seat_already_booked(show: Show, seats: List[Seat]) -> bool

SeatAvailabilityService
    - booking_service: BookingService
    - seat_lock_provider: SeatLockProvider
    ---
    + get_seats_available(show)
    + get_seats_unavailable(show)

PaymentsService:
    - allowed_retries: int
    - seat_lock_provider: SeatLockProvider
    + booking_failures: Dict[Booking, int]
    ---
    + process_payment_failed()
    + process_payment_success() 



